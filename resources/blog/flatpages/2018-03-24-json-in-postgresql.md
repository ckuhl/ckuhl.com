---
title: JSON in PostgreSQL
published: True
category: blog
---

Recently at work, I got into a discussion about whether it makes sense to store
JSON objects in a relational database. While I tried to disagree, they
presented a some convincing arguments. However now that I have had time to
think, I feel as though the arguments also have a few flaws.

Their first argument was that JSON objects are easier to change in the future.
For example, if we had initially assumed that a User can only have one address,
adding a second is as simple as updating the object. No need for database
migrations. It makes sense. However a problem still exists: how do you access
the address on a User? Instead of being a single value, it's now a list of
values. To handle this we need to either modify every existing User, or handle
it in the backend. If we modify every object though, we have effectively
written a database migration. So this is no easier than simply storing our
addresses in a flat table. On the other hand, if we handle this in the backend,
there's a real risk of an exponential increase in complexity. Having two
address formats means there are two ways through the code. If we do this 5 more
times, we have 64 different paths through the code. The overhead and number of
errors is even worse than the temporary headache of writing database
migrations. By using JSON you effectively move the schema for data from the
database to the backend. Where the schema can be enforced automatically with
types in the DB, it is moved into the developer's mind with JSON, adding
one more thing that has to be remembered while dealing with the data.

The other argument presented was that by storing JSON objects, we can store
many types of the same objects. Instead of having a separate table for British
Columbian driver's licences, Ontarian driver's licences, and every other kind,
we could simple store them all in a JSON column on our User. However even
though many things in life may look similar, they may have completely different
properties. If we store all driver's licences as a single JSON object in a
column, it is simple to return a driver's licence. However, what if in the
future, a province allows people to use their licence as a health card? Looking
up a person's health insurance now became much more difficult, as you need to
inspect inside each driver's licence object to determine if that person (1) has
that province's card and (2) uses it as a health card. While this is a
contrived example, I feel the risk cannot be understated. While at the point of
development all use cases could be enumerated, as the world changes you are
left exposed to changes in the outside world.

Despite my complaints, I would agree that JSON (and NoSQL) are hugely valuable
for allowing faster iteration when creating a prototype. That same speed of
iteration however makes it easier to end up worse off than you could end up
with a relational database.

