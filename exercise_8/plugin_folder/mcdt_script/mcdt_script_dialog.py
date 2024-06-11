# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MuensterCityDistrictToolsDialog
                                 A QGIS plugin
 MuensterCityDistrictTools
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-06
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Kjell Wundram
        email                : kwundram@uni-muenster.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# import pdf create function and others
from .create_pdf_profile import *
# import other windows:
from .export_dialog import Ui_Export_Dialog
from .single_district_dialog import Ui_single_district_Dialog

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'mcdt_script_dialog_base.ui'))


class MuensterCityDistrictToolsDialog(QtWidgets.QDialog, FORM_CLASS):
    
    
    
    def open_export_clicked_ui(self):
        
        exDialog= QtWidgets.QDialog()
        ui = Ui_Export_Dialog()
        ui.setupUi(exportDialog)
        #self.exportDialog = ui
        
        exDialog.exec_()
        
    
    def select_output_file(self):
        filename, _filter = QFileDialog.getSaveFileName(self.exportDialog, "Select   output file ","", '*.csv')
        self.exportDialog.output_path_lineEdit.setText(filename)  
             
    def open_single_district_clicked_ui(self):
        
        single_districtDialog= QtWidgets.QDialog()
        ui = Ui_single_district_Dialog()
        ui.setupUi(single_districtDialog)
        
        single_districtDialog.exec_()
        
    
    def __init__(self, parent=None):
        """Constructor."""
        self.exDialog= QtWidgets.QDialog()
        ui = Ui_Export_Dialog()
        ui.setupUi(self.exportDialog)
        self.exportDialog = ui
        super(MuensterCityDistrictToolsDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        
        
        # #widgets-and-dialogs-with-auto-connect
        
        self.setupUi(self)
        self.selectedFeaturesCSVButton.clicked.connect(self.open_export_clicked_ui)
        self.singleDistrictButton.clicked.connect(self.open_single_district_clicked_ui)
        
        
        # export dialog
        #self.exportDialog.output_pushButton.clicked.connect(self.select_output_file)
        
        
