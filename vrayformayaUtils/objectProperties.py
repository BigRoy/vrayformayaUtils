"""
    The `objectProperies` eases managing V-ray object properties nodes..

    It provides a convenient way of doing everything that ``mc.vray("objectProperties", ..)`` does, and more!

    Features
    ========
    Some of the most useful features include the following:

    - **Returns node names**

        The function actually returns the names of the newly created nodes or the ones that have been deleted.

    - **Directly naming new nodes (name parameter)**

        It allows you to name the new objectProperties nodes by using the name parameter.

    - **Apply to nodes list (nodes parameter)**

        Instead of forcing you to operate on the current selection (like Chaosgroup is doing) out method contains a
        nodes parameter that allows you to operate on the list you provide yourself.


    Functions
    =========
"""

import maya.cmds as mc
from vrayformayaUtils.utils import getConnectedSets

def objectProperties(cmd,
                     type=None,
                     nodes=None,
                     name=None):
    """ Adds/removes objectProperties to/from input nodes.

    This is currently an experimental implementation, behaviour and naming of functions/keywords may change.
    Even though our focus is to stay as backwards compatible as possible we can't ensure this in the long run
    for experimental implementations.

    :param cmd: The string command to run for the objectProperties.
                Possible values are: "add_single", "add_multiple", "remove", "remove_sub"
    :type  cmd: str

    :param type: The objectProperties type to operate on. If None provided the default "VRayObjectProperties" is used.
    :type  type: str

    :param nodes: The nodes to operate on. If None provided the current selection is used.
    :type  nodes: list

    :param name: Rename the created nodes to `name`. If None provided nodes will get default name.
    :type  name: str

    :return: If objectProperties nodes are created it returns the newly created nodes. If no nodes have been created,
             but there are related objectProperties nodes that have been deletd those will be returned.

                e.g.

                For "add_single" it will return the newly created objectProperties nodes.

                For "remove" cmd it will return the removed/deleted objectProperties nodes.
    :rtype: list

    """
    # Since the objectProperties command operates on selection when we provide a nodes list
    # we override the selection and store the current selection to set it back afterwards
    if nodes is not None:
        pre_sel = mc.ls(sl=1)
        mc.select(nodes, r=1)

    # Store the currently connected sets of the type that we will be creating
    # Then we can check again afterwards, the new sets not in this old list will be the ones that have been created.
    sel = mc.ls(sl=1)
    if not sel:
        return []

    # We're using the type to filter the connected sets to a list as small as possible. (Optimization)
    # Therefore if None is provided (default is used) we convert it to its actual default type name.
    if type is None:
        type = "VRayObjectProperties"

    pre_connected_sets = set(getConnectedSets(sel, type=type))

    # Create the object properties
    mc.vray("objectProperties", cmd, type)

    # Get the actual objectProperties nodes that have been created
    post_connected_sets = set(getConnectedSets(sel, type=type))
    new_sets = post_connected_sets - pre_connected_sets

    # If there are new sets than the objectProperties commands created something
    if new_sets:
        if name is not None:
            # Rename all nodes and capture the new names directly into the list
            new_sets = [mc.rename(s, name) for s in new_sets]

        if nodes is not None:
            # Since the user might have selected a set that has been deleted by the vray command.
            # We first get the list of pre_sel nodes that actually still exist and select those.
            pre_sel = mc.ls(pre_sel, long=True)
            if pre_sel:
                mc.select(pre_sel, r=1)
            else:
                mc.select(d=1)

        return list(new_sets)

    # If no new sets were created it's likely that something has been deleted instead.
    deleted_sets = pre_connected_sets - post_connected_sets
    if deleted_sets:
        # Return the names of the deleted nodes
        return list(deleted_sets)

    # If we get over here nothing changed.
    return []