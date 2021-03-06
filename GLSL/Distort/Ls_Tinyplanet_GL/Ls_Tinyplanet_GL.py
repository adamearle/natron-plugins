# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Ls_Tinyplanet_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Ls_Tinyplanet_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Ls_Tinyplanet_GL"

def getLabel():
    return "Ls_Tinyplanet_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "Ls_Tinyplanet_GL.png"

def getGrouping():
    return "Community/GLSL/Distort"

def getPluginDescription():
    return "Stereographic reprojection of 360 panoramas."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.07451, 0.5686, 0.4863)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("CAMERA", "Camera")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CAMERA = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat0", "Rotate X : ")
    param.setMinimum(-360, 0)
    param.setMaximum(360, 0)
    param.setDisplayMinimum(-360, 0)
    param.setDisplayMaximum(360, 0)
    param.setDefaultValue(0.2533333, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("X rotation")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat0 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat1", "Rotate Y : ")
    param.setMinimum(-360, 0)
    param.setMaximum(360, 0)
    param.setDisplayMinimum(-360, 0)
    param.setDisplayMaximum(360, 0)
    param.setDefaultValue(-0.7066665999999999, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Y rotation")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat1 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat2", "Zoom : ")
    param.setMinimum(9.999999999999999e-05, 0)
    param.setMaximum(2, 0)
    param.setDisplayMinimum(9.999999999999999e-05, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(0.17, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("zoom")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat2 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createSeparatorParam("TRANSFORM", "Transform")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.TRANSFORM = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createDouble2DParam("Shadertoy1_2mousePosition", "Center : ")
    param.setMinimum(-1.79769e+308, 0)
    param.setMaximum(1.79769e+308, 0)
    param.setDisplayMinimum(-1.79769e+308, 0)
    param.setDisplayMaximum(1.79769e+308, 0)
    param.setMinimum(-1.79769e+308, 1)
    param.setMaximum(1.79769e+308, 1)
    param.setDisplayMinimum(-1.79769e+308, 1)
    param.setDisplayMaximum(1.79769e+308, 1)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setUsePointInteract(True)
    lastNode.Shadertoy1_2mousePosition = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createSeparatorParam("MAP", "Map")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.MAP = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat3", "Lal Mult : ")
    param.setMinimum(-30, 0)
    param.setMaximum(30, 0)
    param.setDisplayMinimum(-30, 0)
    param.setDisplayMaximum(30, 0)
    param.setDefaultValue(0.3183099, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat3 = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat4", "Long Mult : ")
    param.setMinimum(-30, 0)
    param.setMaximum(30, 0)
    param.setDisplayMinimum(-30, 0)
    param.setDisplayMaximum(30, 0)
    param.setDefaultValue(0.1591549, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat4 = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat5", "Lat Offset : ")
    param.setMinimum(-30, 0)
    param.setMaximum(30, 0)
    param.setDisplayMinimum(-30, 0)
    param.setDisplayMaximum(30, 0)
    param.setDefaultValue(-1.570796, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat5 = param
    del param

    param = lastNode.createStringParam("sep16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep16 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat6", "Long Offset : ")
    param.setMinimum(-30, 0)
    param.setMaximum(30, 0)
    param.setDisplayMinimum(-30, 0)
    param.setDisplayMaximum(30, 0)
    param.setDefaultValue(-3.141593, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat6 = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Ls_Tinyplanet_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE105", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE105 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4155, 4060)
    lastNode.setSize(80, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4155, 3517)
    lastNode.setSize(80, 36)
    lastNode.setColor(1, 1, 1)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1")
    lastNode.setPosition(4150, 3790)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(0.2533333, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(-0.7066665999999999, 0)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(0.17, 0)
        del param

    param = lastNode.getParam("paramValueFloat3")
    if param is not None:
        param.setValue(0.3183099, 0)
        del param

    param = lastNode.getParam("paramValueFloat4")
    if param is not None:
        param.setValue(0.1591549, 0)
        del param

    param = lastNode.getParam("paramValueFloat5")
    if param is not None:
        param.setValue(-1.570796, 0)
        del param

    param = lastNode.getParam("paramValueFloat6")
    if param is not None:
        param.setValue(-3.141593, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : Ls_Tinyplanet Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : Ls_Tinyplanet Matchbox for Autodesk Flame\n\n\n// iChannel0: Source,filter=linear,wrap=repeat\n// BBox: iChannel0\n\n// Stereographic projection of a 360x180 latlong panorama, tiny planets style\n// lewis@lewissaunders.com\n\n\nvec2 center = iMouse.xy /iResolution.xy;\n\nuniform float long0 = 0.25333333333; // Rotate X : , min=-10000.0, max=10000\nuniform float lat1 = -0.70666666666; // Rotate Y : , min=-10000.0, max=10000\nuniform float r = 0.17; // Zoom : , min=0.0001, max=2.0\n\nuniform float latm = 0.31830988618379069; // Lal Mult : ,min=-30.0, max=30.0\nuniform float longm = 0.15915494309189535; // Long Mult : ,min=-30.0, max=30.0\nuniform float lato = -1.5707963267948966; // Lat Offset : ,min=-30.0, max=30.0\nuniform float longo = -3.1415926535897932; // Long Offset : ,min=-30.0, max=30.0\n\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec2 res = vec2(iResolution.x, iResolution.y);\n\tvec2 coords = fragCoord.xy / res;\n\tcoords.x -= 0.5;\n\tcoords.x *= (res.x / res.y);\n\tcoords.x += 0.5;\n\n\tfloat p = sqrt((coords.x-center.x)*(coords.x-center.x)+(coords.y-center.y)*(coords.y-center.y));\n\tfloat c = 2.0 * atan(p, 2.0 * r);\n\tfloat longg = (long0 + atan((coords.x-center.x)*sin(c), p*cos(lat1)*cos(c) - (coords.y-center.y)*sin(lat1)*sin(c)));\n\tfloat lat = asin(cos(c)*sin(lat1) + (((coords.y-center.y)*sin(c)*cos(lat1)) / p));\n\tvec2 uv;\n\tuv.x = (longg - longo) * longm;\n\tuv.y = (lat - lato) * latm;\n\n\tvec4 o = texture2D(iChannel0, uv);\n\n\tfragColor = o;\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(7, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("long0")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Rotate X :")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(0.2533333, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(-10000, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(10000, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("lat1")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Rotate Y :")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(-0.7066665999999999, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(-10000, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(10000, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("r")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Zoom :")
        del param

    param = lastNode.getParam("paramDefaultFloat2")
    if param is not None:
        param.setValue(0.17, 0)
        del param

    param = lastNode.getParam("paramMinFloat2")
    if param is not None:
        param.setValue(9.999999999999999e-05, 0)
        del param

    param = lastNode.getParam("paramMaxFloat2")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("latm")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Lal Mult :")
        del param

    param = lastNode.getParam("paramDefaultFloat3")
    if param is not None:
        param.setValue(0.3183099, 0)
        del param

    param = lastNode.getParam("paramMinFloat3")
    if param is not None:
        param.setValue(-30, 0)
        del param

    param = lastNode.getParam("paramMaxFloat3")
    if param is not None:
        param.setValue(30, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("longm")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("Long Mult :")
        del param

    param = lastNode.getParam("paramDefaultFloat4")
    if param is not None:
        param.setValue(0.1591549, 0)
        del param

    param = lastNode.getParam("paramMinFloat4")
    if param is not None:
        param.setValue(-30, 0)
        del param

    param = lastNode.getParam("paramMaxFloat4")
    if param is not None:
        param.setValue(30, 0)
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("lato")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("Lat Offset :")
        del param

    param = lastNode.getParam("paramDefaultFloat5")
    if param is not None:
        param.setValue(-1.570796, 0)
        del param

    param = lastNode.getParam("paramMinFloat5")
    if param is not None:
        param.setValue(-30, 0)
        del param

    param = lastNode.getParam("paramMaxFloat5")
    if param is not None:
        param.setValue(30, 0)
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("longo")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("Long Offset :")
        del param

    param = lastNode.getParam("paramDefaultFloat6")
    if param is not None:
        param.setValue(-3.141593, 0)
        del param

    param = lastNode.getParam("paramMinFloat6")
    if param is not None:
        param.setValue(-30, 0)
        del param

    param = lastNode.getParam("paramMaxFloat6")
    if param is not None:
        param.setValue(30, 0)
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupShadertoy1_2)
    groupShadertoy1_2.connectInput(0, groupSource)

    param = groupShadertoy1_2.getParam("mousePosition")
    group.getParam("Shadertoy1_2mousePosition").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat0")
    group.getParam("Shadertoy1_2paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat1")
    group.getParam("Shadertoy1_2paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat2")
    group.getParam("Shadertoy1_2paramValueFloat2").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat3")
    group.getParam("Shadertoy1_2paramValueFloat3").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat4")
    group.getParam("Shadertoy1_2paramValueFloat4").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat5")
    group.getParam("Shadertoy1_2paramValueFloat5").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat6")
    group.getParam("Shadertoy1_2paramValueFloat6").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Ls_Tinyplanet_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
