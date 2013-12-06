:mod:`objectProperties` Module
==============================

.. automodule:: vrayformayaUtils.objectProperties
    :members:
    :undoc-members:
    :show-inheritance:

Examples
--------

Add multiple displacement objectProperties to selection:

.. code-block:: python

    import vrayformayaUtils as vfm

    vfm.objectProperties.objectProperties(cmd="add_multiple", type="VRayDisplacement")


Add single displacement objectProperties to selection with name `myDisplacementAttributes`:

.. code-block:: python

    import vrayformayaUtils as vfm

    vfm.objectProperties.objectProperties(cmd="add_single", type="VRayDisplacement", name="myDisplacementAttributes")


Remove displacement objectProperties on selection:

.. code-block:: python

    import vrayformayaUtils as vfm

    vfm.objectProperties.objectProperties(cmd="remove", type="VRayDisplacement")

Add displacement properties to all nodes that have the `_DISPLACEMENT` suffix.

.. code-block:: python

    import maya.cmds as mc
    import vrayformayaUtils as vfm

    nodes = mc.ls("*_DISPLACEMENT")
    vfm.objectProperties.objectProperties(cmd="add_single", type="VRayDisplacement", nodes=nodes)
