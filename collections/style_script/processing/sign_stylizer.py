# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterField,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterEnum,
                       QgsApplication,
                       QgsSymbolLayer,
                       QgsProperty,
                       QgsSvgMarkerSymbolLayer)
import processing


class SignStylizer(QgsProcessingAlgorithm):


    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    SIGN_CODE_FIELD = 'sign_code_field'
    SPEED_LIMIT_FIELD = 'speed_limit_field'
    OLD_OR_NEW = "old_or_new"

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return SignStylizer()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'sign_stylizer'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Finnish traffic sign stylizer')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('scripts')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'scripts'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Takes point data layer with Finnish traffic sign codes as input"+
                        " and visualizes each point with the equivalent sign SVG."+
                        " Also determines image size based on map scale.")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """
        self.addParameter(
            QgsProcessingParameterEnum(
                self.OLD_OR_NEW,
                self.tr('Visualisoitko vanhoilla vai uusilla liikennemerkeillä?'),
                ["Vanhoilla", "Uusilla"]
            )
        )
        
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.INPUT,
                self.tr('Valitse liikennemerkkitaso'),
                [QgsProcessing.TypeVectorPoint]
            )
        )



        self.addParameter(
        QgsProcessingParameterField(
                self.SIGN_CODE_FIELD,
                'Valitse sarake, jossa merkkikoodit ovat. Nämä ovat: \n-Digiroad: TYYPPI \n'+
                '-Tierekisteri (Vanhat merkit): S_ASETUSNR \n-Tierekisteri (Uudet merkit): S_UUSIASNR',
                '',
                self.INPUT))
        
        speed_parameter = QgsProcessingParameterField(
                self.SPEED_LIMIT_FIELD,
                'Valitse sarake, jossa liikenteen nopeusrajoitusarvot ovat. \n-Digiroad: ARVO \n'+
                '-Tierekisteri: LMTEKSTI',
                '',
                self.INPUT)
        speed_parameter.setFlags(QgsProcessingParameterField.FlagOptional)
        
        self.addParameter(speed_parameter)

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        """
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )
        """

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        #vector layer given by the user
        input_layer = self.parameterAsVectorLayer(
            parameters,
            self.INPUT,
            context
        )
        
        #the field within previous layer. Should contain numeral codes
        #that identify each traffic sign
        value_field = self.parameterAsString(
                        parameters,
                        self.SIGN_CODE_FIELD,
                        context)
        
        speed_field = self.parameterAsString(
                        parameters,
                        self.SPEED_LIMIT_FIELD,
                        context)
                        
        old_or_new_selection = self.parameterAsString(
                        parameters,
                        self.OLD_OR_NEW,
                        context)
        
        # read user selection on whether to use old or new signs
        # transform this into a usable string
        if old_or_new_selection == "1":
            old_or_new_selection="new"
        else:
            old_or_new_selection="old"
        
        #if the SVG's are installed via Resource sharing, they should be here
        path = (QgsApplication.qgisSettingsDirPath() + "resource_sharing/collections/Väylävirasto"+ 
                " {} traffic signs (Liikennemerkit)/svg/").format(old_or_new_selection)
        #Windows path hijinks
        resource_path = path.replace("\\", "/")
        
        # creating a dummy symbol layer, which will be styled later
        svg_layer = QgsSvgMarkerSymbolLayer("circle")
        
        # creating two expressions, one for defining the path to each SVG image
        # the other for scaling image size based on current map scale
        # the syntax of these strings is the one used in QGIS's Expression bulder
        if (speed_field and old_or_new_selection=="old"):
            path_exp = ("CASE WHEN \"{1}\"=361 AND \"{2}\"=50 THEN concat(\'{0}\', \"{1}\", \'-1.svg\')"+
        " WHEN \"{1}\"=361 AND \"{2}\"=20 THEN concat(\'{0}\', \"{1}\", \'-2.svg\')"+
        " WHEN \"{1}\"=361 AND \"{2}\"=70 THEN concat(\'{0}\', \"{1}\", \'-3.svg\')"+
        " WHEN \"{1}\"=361 AND \"{2}\"=80 THEN concat(\'{0}\', \"{1}\", \'-4.svg\')"+
        " WHEN \"{1}\"=361 AND \"{2}\"=100 THEN concat(\'{0}\', \"{1}\", \'-5.svg\')"+
        " WHEN \"{1}\"=361 AND \"{2}\"=120 THEN concat(\'{0}\', \"{1}\", \'-6.svg\')"+
        " WHEN \"{1}\"=361 AND \"{2}\"=30 THEN concat(\'{0}\', \"{1}\", \'-7.svg\')"+
        " WHEN \"{1}\"=361 AND \"{2}\"=40 THEN concat(\'{0}\', \"{1}\", \'-8.svg\')"+
        " ELSE concat(\'{0}\', \"{1}\", \'.svg\') END").format(resource_path, value_field, speed_field)
        elif (speed_field and old_or_new_selection=="new"):
            path_exp = ("CASE WHEN \"{1}\"= \'C32\' AND \"{2}\"=20 THEN concat(\'{0}\', \"{1}\", \'_2.svg\')"+
        " WHEN \"{1}\"=\'C32\' AND \"{2}\"=30 THEN concat(\'{0}\', \"{1}\", \'_3.svg\')"+
        " WHEN \"{1}\"=\'C32\'AND \"{2}\"=40 THEN concat(\'{0}\', \"{1}\", \'_4.svg\')"+
        " WHEN \"{1}\"=\'C32\' AND \"{2}\"=50 THEN concat(\'{0}\', \"{1}\", \'_5.svg\')"+
        " WHEN \"{1}\"=\'C32\' AND \"{2}\"=70 THEN concat(\'{0}\', \"{1}\", \'_6.svg\')"+
        " WHEN \"{1}\"=\'C32\' AND \"{2}\"=80 THEN concat(\'{0}\', \"{1}\", \'_7.svg\')"+
        " WHEN \"{1}\"=\'C32\' AND \"{2}\"=100 THEN concat(\'{0}\', \"{1}\", \'_8.svg\')"+
        " WHEN \"{1}\"=\'C32\' AND \"{2}\"=120 THEN concat(\'{0}\', \"{1}\", \'_9.svg\')"+
        " ELSE concat(\'{0}\', \"{1}\", \'.svg\') END").format(resource_path, value_field, speed_field)
        else:
            path_exp = "concat(\'{0}\', \"{1}\", \'.svg\')".format(resource_path, value_field)
        size_exp = ("CASE WHEN @map_scale < 10000 THEN 11 WHEN @map_scale < 50000 THEN 8" + 
                    " WHEN @map_scale < 100000 THEN 7 WHEN @map_scale < 150000 THEN 6 WHEN @map_scale < 500000"+ 
                    " THEN 4 ELSE 3 END")
        
        # taking a version of the renderer, which houses the symbol layers
        rend = input_layer.renderer().clone()
        rend.symbol().changeSymbolLayer(0, svg_layer)
        
        # defining the image path expression
        rend.symbol().symbolLayer(0).setDataDefinedProperty(QgsSymbolLayer.PropertyName, 
        QgsProperty.fromExpression(path_exp))
        rend.symbol().symbolLayer(0).setDataDefinedProperty(
        QgsSymbolLayer.PropertySize, QgsProperty.fromExpression(size_exp) )
        
        # setting the new renderer to layer
        input_layer.setRenderer(rend)
        # updating so that the results are shown to the user
        input_layer.triggerRepaint()
        
        return {"Styling":"complete"}

