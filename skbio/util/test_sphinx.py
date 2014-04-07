#!/usr/bin/env python

class someClass(object):
    r"""A test class
    """
    class nestedClass(object):
        r"""A class defined inside a class
        """
        def __init__(self):
            self.sub_works = True


    def __init__(self):
        self.works = False
        self.what = nestedClass()


    def report(self):
        r"""Function that prints the value of "works"

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        This function is just for testing sphinx with nested classes.

        Examples
        --------

        >>> from test_sphinx import someClass
        >>> c = someClass()
        >>> c.report()
        False
        """
        print works
