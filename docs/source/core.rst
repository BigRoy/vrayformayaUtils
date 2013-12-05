:mod:`core` Module
==================

In the ``core`` module you can find quick core functions that ease working with V-ray for Maya data.

For example there's functionality for adding/removing Render Elements

Functions
---------

.. automodule:: vrayformayaUtils.core
    :members:
    :undoc-members:
    :show-inheritance:


Examples
---------

Assuming we want to have a Multi Matte Render Element for the numbers up to 10. We could do something like:

.. code-block:: python

    import maya.cmds as mc
    import vrayformayaUtils as vfm

    nums = 10

    for x in range(0, nums+1, 3):

        # Create the render element
        renderElement = vfm.addRenderElement("MultiMatteElement",
                                             suffix="multimatte{0}-{1}".format(x, x+2))

        # Set the red, blue, green id values.
        mc.setAttr("{0}.vray_redid_multimatte", x)
        mc.setAttr("{0}.vray_blueid_multimatte", x+1)
        mc.setAttr("{0}.vray_greenid_multimatte", x+2)

List all render elements in the scene:

.. code-block:: python

    import maya.cmds as mc
    import vrayformayaUtils as vfm

    print vfm.getRenderElements()