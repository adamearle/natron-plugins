# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Crok_cmyk_halftone_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Crok_cmyk_halftone_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Crok_cmyk_halftone_GL"

def getLabel():
    return "Crok_cmyk_halftone_GL"

def getVersion():
    return 1.01

def getIconPath():
    return "Crok_cmyk_halftone_GL.png"

def getGrouping():
    return "Community/GLSL/Effect"

def getPluginDescription():
    return "GPU accelerated CMYK halftone effect for Shadertoy."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(1, 0.2353, 0.2353)

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

    param = lastNode.createSeparatorParam("SETUP", "Setup")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SETUP = param
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

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat0", "Minimum : ")
    param.setMinimum(0, 0)
    param.setMaximum(20, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(20, 0)
    param.setDefaultValue(2, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat0 = param
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

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat1", "Maximum : ")
    param.setMinimum(0, 0)
    param.setMaximum(20, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(20, 0)
    param.setDefaultValue(4, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat1 = param
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

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat2", "Gain : ")
    param.setMinimum(0, 0)
    param.setMaximum(20, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(20, 0)
    param.setDefaultValue(3, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat2 = param
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

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat3", "Scale : ")
    param.setMinimum(0, 0)
    param.setMaximum(20, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(20, 0)
    param.setDefaultValue(8, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat3 = param
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

    param = lastNode.createSeparatorParam("NAME", "Crok_cmyk_halftone_GL v1.01")

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

    param = lastNode.createSeparatorParam("LINE101", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE101 = param
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

    param = lastNode.createSeparatorParam("CONVERSION", "(Fabrice Fernandez - 2018)")

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

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3647)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1")
    lastNode.setPosition(4139, 3844)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramValueFloat3")
    if param is not None:
        param.setValue(8, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//                                                \r\n//                                                  \r\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM                                        \r\n//                        MM.                          .MM                                \r\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM                  \r\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM     \r\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\r\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\r\n//                   MM.  .MmM              MMMM      MMM.  .MM\r\n//                  MM.  .MMM                 MM       MMM.  .MM\r\n//                 MM.  .MMM            \t   M        MMM.  .MM\r\n//                MM.  .MMM                              MMM.  .MM\r\n//                 MM.  .MMM                            MMM.  .MM\r\n//                  MM.  .MMM       M                  MMM.  .MM\r\n//                   MM.  .MMM      MM                MMM.  .MM\r\n//                    MM.  .MMM     MMM              MMM.  .MM  \r\n//                     MM.  .MMM    MMMM            MMM.  .MM    \r\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM      \r\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM            \r\n//                        MM.                          .MM                 \r\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM                                                      \r\n//                                                                \r\n//\r\n// Adaptation pour Natron par F. Fernandez\r\n// Code original : crok_cmyn_halftone Matchbox pour Autodesk Flame\r\n\r\n// Adapted to Natron by F.Fernandez\r\n// Original code : crok_cmyn_halftone Matchbox for Autodesk Flame\r\n\r\n\r\n// setting inputs names and filtering options\r\n// iChannel0: Source, filter = linear\r\n\r\n// BBox: iChannel0\r\n\r\n\r\nuniform float pMin = 2; // minimum : (minimum), min=0., max=20.\r\nuniform float pMax = 4; // maximum : (maximum), min=0., max=20.\r\n\r\nuniform float pDotsize = 3; // gain : (gain), min=0., max=20.\r\nuniform float pScale = 8; // scale : (scale), min=0., max=20.\r\n\r\nfloat currentFrame = iFrame;\r\n\r\n#define D2R(d) radians(d)\r\n#define SST 0.888\r\n#define SSQ 0.288\r\n\r\nvec2 ORIGIN = 0.5*iResolution.xy;\r\nfloat S = pMin+(pMax-pMin)*(0.5-0.5*cos(0.57*currentFrame));\r\nfloat R = 0.57*0.333*currentFrame;\r\n\r\nvec4 rgb2cmyki(in vec4 c)\r\n{\r\n\tfloat k = max(max(c.r,c.g),c.b);\r\n\treturn min(vec4(c.rgb/k,k),1.0);\r\n}\r\n\r\nvec4 cmyki2rgb(in vec4 c)\r\n{\r\n\treturn vec4(c.rgb*c.a,1.0);\r\n}\r\n\r\nvec2 px2uv(in vec2 px)\r\n{\r\n\treturn vec2(px/iResolution.xy);\r\n}\r\n\r\nvec2 grid(in vec2 px)\r\n{\r\n\t//return px-mod(px,S);\r\n\treturn floor(px/S)*S; // alternate\r\n}\r\n\r\nvec4 ss(in vec4 v)\r\n{\r\n\treturn smoothstep(SST-SSQ,SST+SSQ,v);\r\n}\r\n\r\nvec4 halftone(in vec2 fc,in mat2 m)\r\n{\r\n\tvec2 smp = (grid(m*fc)+0.5*S)*m;\r\n\tfloat s = min(length(fc-smp)/(pDotsize*0.5*S),1.0);\r\n\tvec4 c = rgb2cmyki(texture2D(iChannel0,px2uv(smp+ORIGIN)));\r\n\treturn c+s;\r\n}\r\n\r\nmat2 rotm(in float r)\r\n{\r\n\tfloat cr = cos(r);\r\n\tfloat sr = sin(r);\r\n\treturn mat2(\r\n\t\tcr,-sr,\r\n\t\tsr,cr\r\n\t);\r\n}\r\n\r\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\r\n{\r\n\r\n\t{\r\n\t\tS = pMin+(pMax-pMin)*2.0*abs(pScale-ORIGIN.x)/iResolution.x;\r\n\t\tR = D2R(180.0*(0.0-ORIGIN.y)/iResolution.y);\r\n\t}\r\n\t\r\n\tvec2 fc = fragCoord.xy-ORIGIN;\r\n\t\r\n\tmat2 mc = rotm(R+D2R(15.0));\r\n\tmat2 mm = rotm(R+D2R(75.0));\r\n\tmat2 my = rotm(R);\r\n\tmat2 mk = rotm(R+D2R(45.0));\r\n\t\r\n\tfloat k = halftone(fc,mk).a;\r\n\tvec4 c = cmyki2rgb(ss(vec4(\r\n\t\thalftone(fc,mc).r,\r\n\t\thalftone(fc,mm).g,\r\n\t\thalftone(fc,my).b,\r\n\t\thalftone(fc,mk).a\r\n\t)));\r\n\tfragColor = c;\r\n}\r\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("clamp")
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

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("pMin")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("minimum :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("minimum")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(20, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("pMax")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("maximum :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("maximum")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(20, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("pDotsize")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("gain :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("gain")
        del param

    param = lastNode.getParam("paramDefaultFloat2")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramMinFloat2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat2")
    if param is not None:
        param.setValue(20, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("pScale")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("scale :")
        del param

    param = lastNode.getParam("paramHint3")
    if param is not None:
        param.setValue("scale")
        del param

    param = lastNode.getParam("paramDefaultFloat3")
    if param is not None:
        param.setValue(8, 0)
        del param

    param = lastNode.getParam("paramMinFloat3")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat3")
    if param is not None:
        param.setValue(20, 0)
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1_2)
    groupShadertoy1_2.connectInput(0, groupSource)

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

    try:
        extModule = sys.modules["Crok_cmyk_halftone_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
