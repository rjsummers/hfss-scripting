import ScriptEnv

project_path = r"{{ project_path }}"
output_path = r"{{ output_path }}"
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
