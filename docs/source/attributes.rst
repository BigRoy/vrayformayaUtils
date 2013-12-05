:mod:`attributes` Module
========================

.. automodule:: vrayformayaUtils.attributes
    :members:
    :undoc-members:
    :show-inheritance:

Examples
--------

Adding a subdivision attribute to the current selection:

.. code-block:: python

    import vrayformayaUtils as vfm

    vfm.attributes.vray_subdivision()

The above includes allDescendent shapes. This means if you select a group all it's children and children's children and
so forth are included. You can set the allDescendent parameter to False to exclude those. That way only direct children
shapes are included, so you would have to select the meshes.

Adding a subdivision attribute to the current selection (only direct children shapes):

.. code-block:: python

    import vrayformayaUtils as vfm

    vfm.attributes.vray_subdivision(allDescendents=False)


Adding a subdivision attribute to all objects that end with `_SMOOTH` suffix:

.. code-block:: python

    import maya.cmds as mc
    import vrayformayaUtils as vfm

    nodes = mc.ls("*_SMOOTH")
    vfm.attributes.vray_subdivision(nodes)

If you want to remove an attribute you can set the state parameter to False, like so:

.. code-block:: python

    import vrayformayaUtils as vfm

    # This will remove vray_subdivision attribute from related selected shapes.
    vfm.attributes.vray_subdivision(state=False)
