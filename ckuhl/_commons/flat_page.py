import datetime
import logging
from pathlib import Path
from typing import Any, Dict, Hashable, IO, Tuple

import markdown
import yaml


class FlatPage(object):
    """
    Static representation of a markdown text file with a YAML frontmatter.
    This is used to make loading files into the database easier.
    """
    # Silence the markdown library
    logging.getLogger('MARKDOWN').setLevel(logging.WARNING)

    __log = logging.getLogger(__name__)

    def __init__(self, file_path: Path, root_dir: Path) -> None:
        """Load the file and convert it to a static object"""
        self.file: Path = file_path

        relative_path = file_path.relative_to(root_dir)
        try:
            with file_path.open() as f:
                self.meta: Dict[str, Any] = self.__load_meta(f)
                self.body: str = self.__load_body(f)
        except FileNotFoundError:
            self.__log.error(f'File not found at {relative_path},'
                             f'relative to from root directory {root_dir}')
            self.__log.error(f"The file's absolute path is"
                             f"{file_path.absolute()}")
            raise

        # destructure in two steps so you can spot initialization at a glance
        url, date = self.__get_url_and_date(relative_path)
        self.url: str = url
        self.date: datetime.date = date

    def __str__(self):
        """Unused except for debugging"""
        return f'<FlatPage: {self.meta["title"]}>'

    def __getitem__(self, item: Hashable) -> Any:
        """Used for easy accessing of values in the page meta"""
        return self.meta.get(item)

    @staticmethod
    def __load_meta(file: IO) -> Dict[str, Any]:
        """Given a stream of YAML lines, convert it to a dictionary"""
        lines = []
        next_line = file.readline()

        # read first document separator
        if next_line.strip() != '---':
            raise yaml.YAMLError('The first line must be `---`')
        lines.append(next_line)
        next_line = file.readline()

        # read body
        while next_line.strip() != '---':
            lines.append(next_line)
            try:
                next_line = file.readline()
            except EOFError:
                raise yaml.YAMLError('There must be an ending `---`')

        # TODO: Add optional validation here in the future?

        return yaml.load('\n'.join(lines))

    @staticmethod
    def __load_body(file: IO) -> str:
        """Given a stream of markdown text, produce the HTML equivalent"""
        body = ''.join(file.readlines())
        markdown_extensions = (
            # allows script tags in markdown
            'extra',

            # define abbreviations (e.g. HTML, W3C, &c.)
            'abbr',

            # code highlighting
            'codehilite',

            # use ``` to denote code (instead of spaces)
            'fenced_code',

            # convert ASCII dashes/quotes/ellipses to HTML equiv.
            'smarty',

            # use [^<label>] to use footnotes inline
            'footnotes',
        )
        markdown_configs = {
            'codehilite': {
                'linenums': True,
            },
        }
        # Note: This creates a new Markdown class for each page.
        #       While inefficient, this is only run at startup, and so isn't a
        #       huge problem.
        return markdown.markdown(body,
                                 extensions=markdown_extensions,
                                 configs=markdown_configs)

    @staticmethod
    def __get_url_and_date(path: Path) -> Tuple[str, datetime.date]:
        """
        "Cuts" the date slug of a FlatPage Path and returns the calculated URL
        and date from that
        """
        date_format, date_shape = '%Y-%m-%d', 'YYYY-MM-DD'

        url_path = path.parent.parent.parent
        url = str(url_path / path.stem[len(date_shape) + 1:])

        date = datetime.datetime.strptime(
            path.name[:len(date_shape)], date_format).date()

        return url, date
