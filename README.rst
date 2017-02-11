datedelta
#########

``datedelta.datedelta`` is ``datetime.timedelta`` for date arithmetic.

It can add years, months, or days to dates while accounting for oddities of the
Gregorian calendar. It can also subtract years, months, or days from dates.

Typically, it's useful to compute yearly or monthly subscriptions periods.

Installation
============

.. code-block:: bash

    pip install datedelta

Usage
=====

The most common operations are adding a ``datedelta`` to a ``date`` and
subtracting a ``datedelta`` from a ``date``.

Basic intervals
---------------

The ``YEAR``, ``MONTH``, and ``DAY`` constants allow expressing common
calculations with little code.

.. code-block:: python

    >>> import datetime
    >>> import datedelta

    >>> datetime.date(2016, 1, 1) + datedelta.YEAR
    datetime.date(2017, 1, 1)

    >>> datetime.date(2017, 1, 1) - datedelta.YEAR
    datetime.date(2016, 1, 1)

    >>> datetime.date(2016, 2, 29) + datedelta.YEAR
    datetime.date(2017, 3, 1)

    >>> datetime.date(2017, 3, 1) - datedelta.YEAR
    datetime.date(2016, 3, 1)

    >>> datetime.date(2016, 1, 1) + datedelta.MONTH
    datetime.date(2016, 2, 1)

    >>> datetime.date(2016, 2, 1) - datedelta.MONTH
    datetime.date(2016, 1, 1)

    >>> datetime.date(2016, 1, 31) + datedelta.MONTH
    datetime.date(2016, 3, 1)

    >>> datetime.date(2016, 3, 1) - datedelta.MONTH
    datetime.date(2016, 2, 1)

    >>> datetime.date(2016, 1, 1) + datedelta.DAY
    datetime.date(2016, 1, 2)

    >>> datetime.date(2016, 1, 1) - datedelta.DAY
    datetime.date(2015, 12, 31)

Note that ``datedelta.DAY`` behaves exactly like ``datetime.timedelta(1)``.
It's only provided for consistency.

Arbitrary intervals
-------------------

``datedelta`` objects provide support for arbitrary calculations.

.. code-block:: python

    >>> import datetime
    >>> import datedelta

    >>> datetime.date(2016, 3, 23) + datedelta.datedelta(years=1, months=1, days=-1)
    datetime.date(2017, 4, 22)

    >>> datetime.date(2016, 3, 23) - datedelta.datedelta(years=-1, months=-1, days=1)
    datetime.date(2017, 4, 22)

    >>> datetime.date(2016, 2, 29) + datedelta.datedelta(years=2)
    datetime.date(2018, 3, 1)

    >>> datetime.date(2020, 2, 29) - datedelta.datedelta(years=2)
    datetime.date(2018, 3, 1)

    >>> datetime.date(2016, 2, 29) + datedelta.datedelta(years=2, days=-1)
    datetime.date(2018, 2, 28)

    >>> datetime.date(2020, 2, 29) - datedelta.datedelta(years=2, days=1)
    datetime.date(2018, 2, 28)

    >>> datetime.date(2016, 2, 29) + datedelta.datedelta(years=2, months=6)
    datetime.date(2018, 9, 1)

    >>> datetime.date(2020, 2, 29) - datedelta.datedelta(years=2, months=-6)
    datetime.date(2018, 9, 1)

    >>> datetime.date(2016, 2, 29) + datedelta.datedelta(years=4)
    datetime.date(2020, 2, 29)

    >>> datetime.date(2020, 2, 29) - datedelta.datedelta(years=4)
    datetime.date(2016, 2, 29)

    >>> datetime.date(2016, 2, 29) + datedelta.datedelta(years=4, days=1)
    datetime.date(2020, 3, 1)

    >>> datetime.date(2020, 2, 29) - datedelta.datedelta(years=4, days=-1)
    datetime.date(2016, 3, 1)

    >>> datetime.date(2016, 2, 29) + datedelta.datedelta(years=4, months=6)
    datetime.date(2020, 8, 29)

    >>> datetime.date(2020, 2, 29) - datedelta.datedelta(years=4, months=-6)
    datetime.date(2016, 8, 29)

These results may appear slightly surprising. However, they're consistent, for
reasons explained in the "Behavior" section below.

Other operations
----------------

``datedelta`` instances can be added, subtracted, and multiplied with an
integer. However there are some restrictions on addition and subtraction.

As demonstrated in the "Limitations" section below, adding then subtracting a
given datedelta to a date doesn't always return the original date. In order to
prevent bugs caused by this behavior, when the result of adding or subtracting
two ``datedelta`` isn't well defined, that operation raises ``ValueError``.

.. code-block:: python

    >>> import datedelta

    >>> datedelta.YEAR + datedelta.YEAR
    datedelta.datedelta(years=2)

    >>> 3 * datedelta.YEAR
    datedelta.datedelta(years=3)

    >>> datedelta.YEAR - datedelta.DAY
    datedelta.datedelta(years=1, days=-1)

    >>> datedelta.YEAR - datedelta.YEAR
    Traceback (most recent call last):
        ...
    ValueError: cannot subtract datedeltas with same signs

    >>> datedelta.datedelta(months=6) + datedelta.datedelta(months=-3)
    Traceback (most recent call last):
        ...
    ValueError: cannot add datedeltas with opposite signs

Behavior
========

There are two date arithmetic traps in the Gregorian calendar:

1. Leap years. Problems arise when adding years to a February 29th gives a
   result in a non-leap year.

2. Variable number of days in months. Problems arise when adding months to a
   29th, 30th or 31st gives a result in a month where that day doesn't exist.

In both cases, the result must be changed to the first day of the next month.

This method gives consistent results provided periods are represented by
(start date inclusive, end date exclusive) — that's [start date, end date) if
you prefer the mathematical notation. This representation of periods is akin
to 0-based indexing, which is the convention Python uses.

For example, if someone subscribes for a year starting on 2016-02-29 inclusive,
the end date must be 2017-03-01 exclusive. If it was 2016-02-28 exclusive, the
subscription would be one day too short.

Operations are always performed on years, then months, then days. This order
usually provides the expected behavior. It also minimizes loss of precision.

Limitations
===========

Additions involving ``datedelta`` are neither associative not commutative in
general.

Here are two examples where adding a ``datedelta`` then subtracting it doesn't
return the original value:

.. code-block:: python

    >>> import datetime
    >>> import datedelta

    >>> datetime.date(2020, 2, 29) + datedelta.datedelta(years=1)
    datetime.date(2021, 3, 1)

    >>> datetime.date(2021, 3, 1) - datedelta.datedelta(years=1)
    datetime.date(2020, 3, 1)

    >>> datetime.date(2020, 1, 31) + datedelta.datedelta(months=1)
    datetime.date(2020, 3, 1)

    >>> datetime.date(2020, 3, 1) - datedelta.datedelta(months=1)
    datetime.date(2020, 2, 1)

Here are two examples where adding two ``datedelta`` gives a different result
depending on the order of operations:

.. code-block:: python

    >>> import datetime
    >>> import datedelta

    >>> datetime.date(2016, 2, 29) + datedelta.datedelta(months=6) + datedelta.datedelta(years=1)
    datetime.date(2017, 8, 29)

    >>> datetime.date(2016, 2, 29) + datedelta.datedelta(years=1) + datedelta.datedelta(months=6)
    datetime.date(2017, 9, 1)

    >>> datetime.date(2016, 1, 31) + datedelta.datedelta(months=2) + datedelta.datedelta(months=5)
    datetime.date(2016, 8, 31)

    >>> datetime.date(2016, 1, 31) + datedelta.datedelta(months=5) + datedelta.datedelta(months=2)
    datetime.date(2016, 9, 1)

To avoid problems, you should always start from the same reference date and add
a single ``datedelta``. Don't chain additions or subtractions.

To minimize the risk of incorrect results, ``datedelta`` only implements
operations that have unambiguous semantics:

* Adding a datedelta to a date
* Subtracting a datedelta from a date
* Adding a datedelta to a datedelta when components have the same sign
* Subtracting a datedelta from a datedelta when components have opposite signs

(PEP 20 says: "In the face of ambiguity, refuse the temptation to guess.")

Alternatives
============

``datedelta.datedelta`` is smarter than ``datetime.timedelta`` because it knows
about years and months in addition to days.

``datedelta.datedelta`` provides a subset of the features found in
``dateutil.relativedelta``. Not only does it only support dates, but:

* It omits the "replace" behavior which is very error-prone.
* It doesn't allow explicit control of leapdays.
* It uses keyword-only arguments.
* It requires Python 3.

Handling leap days automatically reduces the number of choices the programmer
must make and thus the number of errors they can make.

Note that ``datedelta.datedelta`` adjusts non-existing days to the first day of
the next month while ``dateutil.relativedelta`` adjusts them to the last day of
the current month.

If you're stuck with Python 2, just copy the code, make ``datedelta`` inherit
from ``object``, and remove the ``*`` in the signature of ``__init__``.

If you're comfortable with ``dateutil`` and don't mind its larger footprint,
there's little to gain by switching to ``datedelta``.

Changelog
=========

1.2
---

* Optimize hashing and pickling.

1.1
---

* Add ``YEAR``, ``MONTH``, and ``DAY`` constants.

1.0
---

* Initial stable release.
