# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2019.2.0
# 13:33:48  Jul 03, 2020
# ----------------------------------------------
import ScriptEnv

project_path = 'F:/Dropbox/dev/hfss-scripting/rectangular_waveguide.aedt'
output_path = ('F:/Dropbox/dev/hfss-scripting/' +
               'rectangular_waveguide_HFSSDesign1.s2p')
z0 = 500

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.OpenProject(project_path)
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("Solutions")
oModule.ExportNetworkData(oDesign.GetNominalVariation(), ["Setup1:Sweep"], 3,
                          output_path, ["all"], True, z0, "S", -1, 2,
                          15, True, False, False)
