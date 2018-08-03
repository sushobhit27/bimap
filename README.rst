==========
Bimap
==========

Bimap is a bidirectional dictionary, similar to boost bimap.

------------------------
Usage
------------------------

.. code-block:: python

    from bimap import Bimap
    bm = Bimap()
    bm.left[1] = 'a'
    bm.left[2] = 'b'
    bm.left[3] = 'c'
    
    assert bm.left[2] == 'b'
    assert bm.right['c'] == 3

.. code-block::

------------------------
Installation
------------------------

.. code-block::

  pip install bimap
