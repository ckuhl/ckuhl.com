from django import test

from _commons.templatetags.html_tags import first_paragraph_html


class TestCommonsModels(test.TestCase):
    # TODO: How does one test a model?
    ...


class TestCommonsTemplateTags(test.TestCase):
    def test_template_tag_empty_string(self):
        self.assertEqual(first_paragraph_html(''), '')

    def test_template_tag_one_para(self):
        s = '<p>This is a paragraph.</p>'
        self.assertEqual(first_paragraph_html(s), s)

    def test_template_tag_line_break(self):
        s = '<p>This\nis\na\nparagraph.\n</p><p>So is this!</p>'
        self.assertEqual(first_paragraph_html(s),
                         '<p>This\nis\na\nparagraph.\n</p>')
