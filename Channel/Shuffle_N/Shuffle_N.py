# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Shuffle_NExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Shuffle_NExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Shuffle_N"

def getLabel():
    return "Shuffle_N"

def getVersion():
    return 1

def getIconPath():
    return "Shuffle_N.png"

def getGrouping():
    return "Community/Channel"

def getPluginDescription():
    return "Inverted Shuufle node."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Shuffle_N")
    param = lastNode.createStringParam("separator02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator02 = param
    del param

    param = lastNode.createStringParam("separator01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator01 = param
    del param

    param = lastNode.createChoiceParam("Shuffle1outputLayer", "Output Plane")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Shuffle1outputLayer = param
    del param

    param = lastNode.createChoiceParam("Shuffle1outputComponents", "Output Components")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Shuffle1outputComponents = param
    del param

    param = lastNode.createChoiceParam("Shuffle1outputPremult", "Output Premult")
    param.setDefaultValue(2)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Shuffle1outputPremult = param
    del param

    param = lastNode.createChoiceParam("Choice_R", "R")
    entries = [ ("B.Color.R", ""),
    ("B.Color.G", ""),
    ("B.Color.B", ""),
    ("B.Color.A", ""),
    ("0", ""),
    ("1", ""),
    ("A.Color.R", ""),
    ("A.Color.G", ""),
    ("A.Color.B", ""),
    ("A.Color.A", ""),
    ("0", ""),
    ("1", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Choice_R = param
    del param

    param = lastNode.createChoiceParam("Choice_G", "G")
    entries = [ ("B.Color.R", ""),
    ("B.Color.G", ""),
    ("B.Color.B", ""),
    ("B.Color.A", ""),
    ("0", ""),
    ("1", ""),
    ("A.Color.R", ""),
    ("A.Color.G", ""),
    ("A.Color.B", ""),
    ("A.Color.A", ""),
    ("0", ""),
    ("1", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("B.Color.G")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Choice_G = param
    del param

    param = lastNode.createChoiceParam("Choice_B", "B")
    entries = [ ("B.Color.R", ""),
    ("B.Color.G", ""),
    ("B.Color.B", ""),
    ("B.Color.A", ""),
    ("0", ""),
    ("1", ""),
    ("A.Color.R", ""),
    ("A.Color.G", ""),
    ("A.Color.B", ""),
    ("A.Color.A", ""),
    ("0", ""),
    ("1", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("B.Color.B")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Choice_B = param
    del param

    param = lastNode.createChoiceParam("Choice_A", "A")
    entries = [ ("B.Color.R", ""),
    ("B.Color.G", ""),
    ("B.Color.B", ""),
    ("B.Color.A", ""),
    ("0", ""),
    ("1", ""),
    ("A.Color.R", ""),
    ("A.Color.G", ""),
    ("A.Color.B", ""),
    ("A.Color.A", ""),
    ("0", ""),
    ("1", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("B.Color.A")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Choice_A = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("separator19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator19 = param
    del param

    param = lastNode.createStringParam("separator20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator20 = param
    del param

    param = lastNode.createSeparatorParam("line02", "Shuffle_N")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line02 = param
    del param

    param = lastNode.createStringParam("separator21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator21 = param
    del param

    param = lastNode.createStringParam("separator22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator22 = param
    del param

    param = lastNode.createSeparatorParam("line03", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line03 = param
    del param

    param = lastNode.createStringParam("separator23", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator23 = param
    del param

    param = lastNode.createStringParam("separator24", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator24 = param
    del param

    param = lastNode.createSeparatorParam("conversion", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.conversion = param
    del param

    param = lastNode.createStringParam("separator25", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator25 = param
    del param

    param = lastNode.createStringParam("separator26", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator26 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(4149, 3671)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.R")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.G")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.B")
        del param

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "A_2"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("A_2")
    lastNode.setLabel("A")
    lastNode.setPosition(4079, 3524)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupA_2 = lastNode

    del lastNode
    # End of node "A_2"

    # Start of node "B_2"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("B_2")
    lastNode.setLabel("B")
    lastNode.setPosition(4223, 3528)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupB_2 = lastNode

    del lastNode
    # End of node "B_2"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(4149, 3873)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupShuffle1.connectInput(0, groupA_2)
    groupShuffle1.connectInput(1, groupB_2)
    groupOutput1.connectInput(0, groupShuffle1)

    param = groupShuffle1.getParam("outputLayer")
    group.getParam("Shuffle1outputLayer").setAsAlias(param)
    del param
    param = groupShuffle1.getParam("outputComponents")
    group.getParam("Shuffle1outputComponents").setAsAlias(param)
    del param
    param = groupShuffle1.getParam("outputPremult")
    group.getParam("Shuffle1outputPremult").setAsAlias(param)
    del param
    param = groupShuffle1.getParam("outputR")
    param.setExpression("thisGroup.Choice_R.get()", False, 0)
    del param
    param = groupShuffle1.getParam("outputG")
    param.setExpression("thisGroup.Choice_G.get()", False, 0)
    del param
    param = groupShuffle1.getParam("outputB")
    param.setExpression("thisGroup.Choice_B.get()", False, 0)
    del param
    param = groupShuffle1.getParam("outputA")
    param.setExpression("thisGroup.Choice_A.get()", False, 0)
    del param

    try:
        extModule = sys.modules["Shuffle_NExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
