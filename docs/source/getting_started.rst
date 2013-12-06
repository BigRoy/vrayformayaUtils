Getting Started
===============

Ok. So you have installed the ``vrayformayaUtils`` package and your urge to get started using it is huge.

Well let's get started and open your version of choice of Maya.

Create some objects of your own or run the script below for a simple testing environment that contains some polygon
meshes, nurbsSurfaces and nurbsCurves.

.. code-block:: python

    import maya.cmds as mc
    import random

    funcs = mc.polyCube, mc.polySphere, mc.sphere, mc.circle

    amount = 10
    offset = -amount/2.0
    spacing_size = 2.0
    for x in range(amount):
        for y in range(amount):
            object = random.choice(funcs)()
            mc.move(spacing_size*(offset+x),
                    spacing_size*(offset+y),
                    0,
                    object)

Your scene is looking great. Because you're a V-ray fan you've already double checked whether V-ray for Maya is loaded
in the plug-in manager. If you didn't then make sure you do now.


Adding V-ray Attributes
-----------------------

So some of our objects might be polygon meshes that we want to smooth in our V-ray renders. A way to doing that is
by using v-ray attributes, specifically the **V-ray Subdivision attribute**.

Select all the meshes that you want to give the v-ray subdivision attribute and run:

.. code-block:: python

    import vrayformayaUtils as vfm

    vfm.attributes.vray_subdivision()

Without any parameters the attribute functions will always apply to your current selection, easy! But what if you have
a list of nodes that you acquired through some extensive pipeline you might have already developed. Every attribute
functions first argument is its input list that it will operate on, only when that argument is not provided (and is None)
it will use your selection.

So to apply it to only the meshes in our scene that start with ``pSphere`` we can do:

.. code-block:: python

    import maya.cmds as mc
    import vrayformayaUtils as vfm

    nodes = mc.ls("pSphere*")
    vfm.attributes.vray_subdivision(nodes)


To find out more about working with v-ray attributes have a look at the :doc:`attributes` documentation.


Adding V-Ray Render Elements
----------------------------

Let's try something else. Maybe working with **RenderElements**?

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


You can also directly try setting its values through the ``vfm.addRenderElement`` function, but it's currently still an
experimental functionality. You could do:

.. code-block:: python

    import maya.cmds as mc
    import vrayformayaUtils as vfm

    nums = 10

    for x in range(0, nums+1, 3):

        # Create the render element
        renderElement = vfm.addRenderElement("MultiMatteElement",
                                             suffix="multimatte{0}-{1}".format(x, x+2),
                                             vray_redid_multimatte=x,
                                             vray_blueid_multimatte=x+1,
                                             vray_greenid_multimatte=x+2)

Fore more information about the core functions have a look at the :doc:`core` documentation.

Adding V-Ray Object Properties
------------------------------

Currently we have an experimental implementation that should already give you full control over your v-ray object
properties.

To add some ``VRayObjectProperties`` to your current selection:

.. code-block:: python

    import vrayformayaUtils as vfm

    vfm.objectProperties.objectProperties("add_single", "VRayObjectProperties")


To remove the ``VRayObjectProperties`` on your current selection:

.. code-block:: python

    import vrayformayaUtils as vfm

    vfm.objectProperties.objectProperties("remove", "VRayObjectProperties")

To add the ``VRayDisplacement`` object properties seperate to every object in your current selection:

.. code-block:: python

    import vrayformayaUtils as vfm

    vfm.objectProperties.objectProperties("add_multiple", "VRayDisplacement")

To add the ``VRayRenderableCurve`` object properties to all nurbsCurves in your scene and name the node
``renderCurveProperties``:

.. code-block:: python

    import maya.cmds as mc
    import vrayformayaUtils as vfm

    nodes = mc.ls(type="nurbsCurve")
    vfm.objectProperties.objectProperties("add_single", "VRayRenderableCurve", nodes=nodes, name="renderCurveProperties")

Fore more information about the objectProperties functions have a look at the :doc:`objectProperties` documentation.