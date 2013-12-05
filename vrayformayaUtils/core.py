import maya.cmds as mc
import maya.mel as mel

def getRenderElementClassType(renderElement):
    """ Return the vrayClassType from a render element node.

        :param renderElement: The name of the render element node.
        :type renderElement: str, unicode

        :rtype: str
    """
    attr = "{0}.vrayClassType".format(renderElement)
    return mc.getAttr(attr)


def getRenderElements(renderElements=None, vrayClassType=None):
    """ Returns the render elements in the scene.

        :param renderElements: An input list to get render elements from. If None it will use ALL nodes in the scene.
        :type  renderElements: list, None

        :param vrayClassType: Filter the return list to only render elements of the vrayClassTypes provided.
                              If None it will not filter the list.
        :type  vrayClassType: str, tuple

        :returns: A list of render element node names.
        :rtype: list
    """
    if renderElements is None:
        renderElements = mc.ls(type="VRayRenderElement")
    else:
        renderElements = mc.ls(renderElements, type="VRayRenderElement")

    if not renderElements:
        return []

    if vrayClassType:
        if not isinstance(vrayClassType, (tuple, list)):
            vrayClassType = set([vrayClassType])
        else:
            vrayClassType = set(vrayClassType)

        renderElements = [x for x in renderElements if getRenderElementClassType(x) in vrayClassType]

    return renderElements


def addRenderElement(vrayClassType, enabled=True, name=None, suffix=None, **kwargs):
    """ Create a V-ray Render Element based on vrayClassType.

        Tip: When clicking once on a render element in the "Available Render Elements" list in the render settings it
             will print out something like: `vrayAddRenderElement X;` where X is the name of the vrayClassType.
             You can use that name to create that renderLayer through this command as well.

        Tip: You could also get a list of all available render elements class types by doing:
             import maya.cmds as mc
             print mc.vray("getRenderElements")

        :param enabled: Enable/disable the created render element. (default: True)
        :type  enabled: bool

        :param name: If provided this allows you to set the name of the created render element node.
        :type  name: None or str

        :param suffix: The filename suffix for the render element. (default: name of the created node)
        :type  suffix: None or str

        :param kwargs: The attributes that are available on the render element after creation can directly be set
                       through keyword arguments. Assuming that the attributes start with 'vray'. This is an
                       experimental implementation but is likely to stay.

        :return: The name of the node created
        :rtype: str
    """
    node = mel.eval("vrayAddRenderElement {0}".format(vrayClassType))

    if name is not None:
        node = mc.rename(node, name)

    if not enabled:
        mc.setAttr("{0}.enabled".format(node), enabled)

    if suffix is not None:
        mc.setAttr("{0}.vray_name_multimatte".format(node), suffix, type="string")

    for kw, value in kwargs:
        if kw.startswith("vray"):
            nodeAttr = "{0}.{1}".format(node, kw)
            if not mc.objExists(nodeAttr):
                mc.warning("{0} doesn't exist. You have likely entered an invalid attribute keyword.".format(nodeAttr))
            else:
                if isinstance(value, basestring):
                    mc.setAttr(nodeAttr, value, type="string")
                else:
                    mc.setAttr(nodeAttr, value)

    return node