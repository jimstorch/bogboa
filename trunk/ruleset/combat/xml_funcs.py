#--[ getText ]------------------------------------------------------------------
# From somewhere
def getText(self, nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    rc = str(rc)
    return rc

#--[ Indent ]------------------------------------------------------------------
# From http://effbot.org/zone/element-lib.htm (plus Paul Du Bois's comment)

def indent(elem, level=0):

    """Make an ElementTree all nice and pretty with indents and line breaks."""

    i = "\n" + level * "    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        for child in elem:
            indent(child, level+1)
        if not child.tail or not child.tail.strip():
            child.tail = i
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
