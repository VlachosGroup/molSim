Search.setIndex({docnames:["AIMSim","AIMSim.chemical_datastructures","AIMSim.ops","AIMSim.tasks","AIMSim.utils","README","implemented_metrics","index","interfaces","interfaces.UI","modules","molSim.chemical_datastructures","molSim.ops","molSim.tasks","molSim.utils","setup","test","tests"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":4,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,sphinx:56},filenames:["AIMSim.rst","AIMSim.chemical_datastructures.rst","AIMSim.ops.rst","AIMSim.tasks.rst","AIMSim.utils.rst","README.rst","implemented_metrics.rst","index.rst","interfaces.rst","interfaces.UI.rst","modules.rst","molSim.chemical_datastructures.rst","molSim.ops.rst","molSim.tasks.rst","molSim.utils.rst","setup.rst","test.rst","tests.rst"],objects:{"":[[0,0,0,"-","AIMSim"],[8,0,0,"-","interfaces"],[16,0,0,"-","test"],[17,0,0,"-","tests"]],"AIMSim.chemical_datastructures":[[1,0,0,"-","molecule"],[1,0,0,"-","molecule_set"]],"AIMSim.chemical_datastructures.molecule":[[1,1,1,"","Molecule"]],"AIMSim.chemical_datastructures.molecule.Molecule":[[1,2,1,"","draw"],[1,2,1,"","get_descriptor_val"],[1,2,1,"","get_mol_property_val"],[1,2,1,"","get_name"],[1,2,1,"","get_similarity_to"],[1,2,1,"","is_same"],[1,2,1,"","match_fingerprint_from"],[1,2,1,"","set_descriptor"]],"AIMSim.chemical_datastructures.molecule_set":[[1,1,1,"","MoleculeSet"]],"AIMSim.chemical_datastructures.molecule_set.MoleculeSet":[[1,2,1,"","cluster"],[1,2,1,"","compare_against_molecule"],[1,2,1,"","get_cluster_labels"],[1,2,1,"","get_distance_matrix"],[1,2,1,"","get_mol_names"],[1,2,1,"","get_mol_properties"],[1,2,1,"","get_most_dissimilar_pairs"],[1,2,1,"","get_most_similar_pairs"],[1,2,1,"","get_pairwise_similarities"],[1,2,1,"","get_property_of_most_dissimilar"],[1,2,1,"","get_property_of_most_similar"],[1,2,1,"","get_similarity_matrix"],[1,2,1,"","get_transformed_descriptors"],[1,2,1,"","is_present"]],"AIMSim.exceptions":[[0,3,1,"","InvalidConfigurationError"],[0,3,1,"","LoadingError"],[0,3,1,"","MordredCalculatorError"],[0,3,1,"","NotInitializedError"]],"AIMSim.ops":[[2,0,0,"-","clustering"],[2,0,0,"-","descriptor"],[2,0,0,"-","similarity_measures"]],"AIMSim.ops.clustering":[[2,1,1,"","Cluster"]],"AIMSim.ops.clustering.Cluster":[[2,2,1,"","fit"],[2,2,1,"","get_labels"],[2,2,1,"","predict"]],"AIMSim.ops.descriptor":[[2,1,1,"","Descriptor"]],"AIMSim.ops.descriptor.Descriptor":[[2,2,1,"","check_init"],[2,2,1,"","fold_to_equal_length"],[2,2,1,"","get_all_supported_descriptors"],[2,2,1,"","get_folded_fprint"],[2,2,1,"","get_label"],[2,2,1,"","get_params"],[2,2,1,"","get_supported_fprints"],[2,2,1,"","is_fingerprint"],[2,2,1,"","make_fingerprint"],[2,2,1,"","set_manually"],[2,2,1,"","shorten_label"],[2,2,1,"","to_numpy"],[2,2,1,"","to_rdkit"]],"AIMSim.ops.similarity_measures":[[2,1,1,"","SimilarityMeasure"]],"AIMSim.ops.similarity_measures.SimilarityMeasure":[[2,2,1,"","get_compatible_metrics"],[2,2,1,"","get_supported_binary_metrics"],[2,2,1,"","get_supported_general_metrics"],[2,2,1,"","get_supported_metrics"],[2,2,1,"","get_uniq_metrics"],[2,2,1,"","is_distance_metric"]],"AIMSim.tasks":[[3,0,0,"-","cluster_data"],[3,0,0,"-","compare_target_molecule"],[3,0,0,"-","identify_outliers"],[3,0,0,"-","measure_search"],[3,0,0,"-","see_property_variation_with_similarity"],[3,0,0,"-","task"],[3,0,0,"-","task_manager"],[3,0,0,"-","visualize_dataset"]],"AIMSim.tasks.cluster_data":[[3,1,1,"","ClusterData"]],"AIMSim.tasks.compare_target_molecule":[[3,1,1,"","CompareTargetMolecule"]],"AIMSim.tasks.compare_target_molecule.CompareTargetMolecule":[[3,2,1,"","get_hits_dissimilar_to"],[3,2,1,"","get_hits_similar_to"]],"AIMSim.tasks.identify_outliers":[[3,1,1,"","IdentifyOutliers"]],"AIMSim.tasks.measure_search":[[3,1,1,"","MeasureSearch"]],"AIMSim.tasks.measure_search.MeasureSearch":[[3,2,1,"","get_best_measure"]],"AIMSim.tasks.see_property_variation_with_similarity":[[3,1,1,"","SeePropertyVariationWithSimilarity"]],"AIMSim.tasks.see_property_variation_with_similarity.SeePropertyVariationWithSimilarity":[[3,2,1,"","get_property_correlations_in_most_dissimilar"],[3,2,1,"","get_property_correlations_in_most_similar"]],"AIMSim.tasks.task":[[3,1,1,"","Task"]],"AIMSim.tasks.task_manager":[[3,1,1,"","TaskManager"]],"AIMSim.tasks.visualize_dataset":[[3,1,1,"","VisualizeDataset"]],"AIMSim.utils":[[4,0,0,"-","ccbmlib_fingerprints"],[4,0,0,"-","plotting_scripts"]],"AIMSim.utils.ccbmlib_fingerprints":[[4,4,1,"","atom_pairs"],[4,4,1,"","avalon"],[4,4,1,"","generate_fingerprints"],[4,4,1,"","hash_parameter_set"],[4,4,1,"","hashed_atom_pairs"],[4,4,1,"","hashed_morgan"],[4,4,1,"","hashed_torsions"],[4,4,1,"","maccs_keys"],[4,4,1,"","morgan"],[4,4,1,"","rdkit_fingerprint"],[4,4,1,"","to_key_val_string"],[4,4,1,"","torsions"]],"AIMSim.utils.plotting_scripts":[[4,4,1,"","plot_barchart"],[4,4,1,"","plot_density"],[4,4,1,"","plot_heatmap"],[4,4,1,"","plot_multiple_barchart"],[4,4,1,"","plot_parity"],[4,4,1,"","plot_scatter"]],"interfaces.config_reader":[[8,4,1,"","main"]],"tests.test_CompareTargetMolecule":[[17,1,1,"","TestCompareTargetMolecule"]],"tests.test_CompareTargetMolecule.TestCompareTargetMolecule":[[17,2,1,"","smiles_seq_to_xl_or_csv"],[17,2,1,"","tearDownClass"],[17,2,1,"","test_get_molecule_least_similar_to"],[17,2,1,"","test_get_molecule_most_similar_to"]],"tests.test_Descriptor":[[17,1,1,"","TestDescriptor"]],"tests.test_Descriptor.TestDescriptor":[[17,2,1,"","test_bad_descriptors_padelpy_descriptors"],[17,2,1,"","test_descriptor_arbitrary_list_init"],[17,2,1,"","test_descriptor_arbitrary_numpy_init"],[17,2,1,"","test_descriptor_empty_init"],[17,2,1,"","test_descriptor_make_fingerprint"],[17,2,1,"","test_fingerprint_folding"],[17,2,1,"","test_mordred_descriptors"],[17,2,1,"","test_nonexistent_mordred_descriptors"],[17,2,1,"","test_padelpy_descriptors"],[17,2,1,"","test_topological_fprint_min_path_lesser_than_atoms"]],"tests.test_LoadingErrorException":[[17,1,1,"","TestLoadingERrorException"]],"tests.test_LoadingErrorException.TestLoadingERrorException":[[17,2,1,"","test_invalid_pdb"],[17,2,1,"","test_invalid_smiles"],[17,2,1,"","test_missing_pdb"],[17,2,1,"","test_missing_smiles"]],"tests.test_MeasureSearch":[[17,1,1,"","TestMeasureSearch"]],"tests.test_MeasureSearch.TestMeasureSearch":[[17,2,1,"","smiles_seq_to_textfile"],[17,2,1,"","test_error_optim_algo"],[17,2,1,"","test_fixed_SimilarityMeasure"],[17,2,1,"","test_fixed_fprint"],[17,2,1,"","test_logfile_generation"],[17,2,1,"","test_max_optim_algo"],[17,2,1,"","test_min_optim_algo"],[17,2,1,"","test_msearch_completion"],[17,2,1,"","test_msearch_init"],[17,2,1,"","test_msearch_init_error"],[17,2,1,"","test_only_metric_fixed_fprint_search"],[17,2,1,"","test_only_metric_fixed_measure_search"],[17,2,1,"","test_only_metric_search"],[17,5,1,"","test_smiles"],[17,2,1,"","test_verbose_output"]],"tests.test_Molecule":[[17,1,1,"","TestMolecule"]],"tests.test_Molecule.TestMolecule":[[17,2,1,"","test_get_name"],[17,2,1,"","test_get_property_value"],[17,2,1,"","test_is_same"],[17,2,1,"","test_match_fprint_error"],[17,2,1,"","test_mol_mol_similarity_w_morgan_tanimoto"],[17,2,1,"","test_mol_smiles_loadingerror"],[17,2,1,"","test_mol_src_pdb_loadingerror"],[17,2,1,"","test_mol_src_txt_loadingerror"],[17,2,1,"","test_molecule_created_w_attributes"],[17,2,1,"","test_molecule_created_with_no_attributes"],[17,2,1,"","test_molecule_draw"],[17,2,1,"","test_molecule_graph_similar_to_itself_morgan_dice"],[17,2,1,"","test_molecule_graph_similar_to_itself_morgan_l0"],[17,2,1,"","test_molecule_graph_similar_to_itself_morgan_tanimoto"],[17,2,1,"","test_set_molecule_from_file"],[17,2,1,"","test_set_molecule_from_smiles"]],"tests.test_MoleculeSet":[[17,1,1,"","TestMoleculeSet"]],"tests.test_MoleculeSet.TestMoleculeSet":[[17,2,1,"","smarts_seq_to_smiles_file"],[17,2,1,"","smiles_seq_to_pdb_dir"],[17,2,1,"","smiles_seq_to_smi_file"],[17,2,1,"","smiles_seq_to_smiles_file"],[17,2,1,"","smiles_seq_to_textfile"],[17,2,1,"","smiles_seq_to_xl_or_csv"],[17,2,1,"","test_clustering_fingerprints"],[17,2,1,"","test_get_most_dissimilar_pairs"],[17,2,1,"","test_get_most_similar_pairs"],[17,2,1,"","test_invalid_transform_error"],[17,2,1,"","test_mds_transform"],[17,2,1,"","test_molecule_set_getters"],[17,2,1,"","test_molecule_set_sim_getters"],[17,2,1,"","test_pca_transform"],[17,2,1,"","test_set_molecule_database_fingerprint_from_csv"],[17,2,1,"","test_set_molecule_database_from_csv"],[17,2,1,"","test_set_molecule_database_from_excel"],[17,2,1,"","test_set_molecule_database_from_pdb_dir"],[17,2,1,"","test_set_molecule_database_from_smarts_file"],[17,2,1,"","test_set_molecule_database_from_smi_file"],[17,2,1,"","test_set_molecule_database_from_smiles_file"],[17,2,1,"","test_set_molecule_database_from_textfile"],[17,2,1,"","test_set_molecule_database_w_descriptor_property_from_csv"],[17,2,1,"","test_set_molecule_database_w_descriptor_property_from_excel"],[17,2,1,"","test_set_molecule_database_w_fingerprint_similarity_from_csv"],[17,2,1,"","test_set_molecule_database_w_property_from_csv"],[17,2,1,"","test_set_molecule_database_w_property_from_excel"],[17,2,1,"","test_set_molecule_database_w_property_from_textfile"],[17,2,1,"","test_set_molecule_database_w_similarity_from_csv"],[17,5,1,"","test_smarts"],[17,5,1,"","test_smiles"],[17,2,1,"","test_subsample_molecule_database_from_csv"],[17,2,1,"","test_subsample_molecule_database_from_excel"],[17,2,1,"","test_subsample_molecule_database_from_pdb_dir"],[17,2,1,"","test_subsample_molecule_database_from_textfile"],[17,2,1,"","test_tsne_transform"]],"tests.test_SimilarityMeasure":[[17,1,1,"","TestSimilarityMeasure"]],"tests.test_SimilarityMeasure.TestSimilarityMeasure":[[17,2,1,"","smiles_seq_to_xl_or_csv"],[17,2,1,"","test_all_supported_measures"],[17,2,1,"","test_get_abcd"],[17,2,1,"","test_similarity_measure_limits"]],"tests.test_SimilarityMeasureValueErrors":[[17,1,1,"","TestSimilarityMeasureValueError"]],"tests.test_SimilarityMeasureValueErrors.TestSimilarityMeasureValueError":[[17,2,1,"","test_binary_only_metrics"],[17,2,1,"","test_compatible_metrics"],[17,2,1,"","test_empty_fprints"],[17,2,1,"","test_invalid_metric"],[17,2,1,"","test_vectornorm_length_errors"]],"tests.test_TaskManager":[[17,1,1,"","TestTaskManager"]],"tests.test_TaskManager.TestTaskManager":[[17,2,1,"","setUpClass"],[17,2,1,"","test_no_tasks_task_manager"],[17,2,1,"","test_task_manager"]],"tests.test_multithreading":[[17,1,1,"","TestMultithreading"]],"tests.test_multithreading.TestMultithreading":[[17,2,1,"","setUpClass"],[17,2,1,"","tearDownClass"],[17,2,1,"","test_multithreading_autoconfig"],[17,2,1,"","test_multithreading_consistency_10_threads"],[17,2,1,"","test_multithreading_consistency_2_threads"],[17,2,1,"","test_multithreading_consistency_3_threads"],[17,2,1,"","test_multithreading_consistency_4_threads"],[17,2,1,"","test_multithreading_consistency_5_threads"],[17,2,1,"","test_multithreading_consistency_6_threads"],[17,2,1,"","test_multithreading_consistency_7_threads"],[17,2,1,"","test_speedup_efficiency_cosine"],[17,2,1,"","test_speedup_efficiency_tanimoto"]],AIMSim:[[1,0,0,"-","chemical_datastructures"],[0,0,0,"-","exceptions"],[2,0,0,"-","ops"],[3,0,0,"-","tasks"],[4,0,0,"-","utils"]],interfaces:[[9,0,0,"-","UI"],[8,0,0,"-","config_reader"]],tests:[[17,0,0,"-","test_CompareTargetMolecule"],[17,0,0,"-","test_Descriptor"],[17,0,0,"-","test_LoadingErrorException"],[17,0,0,"-","test_MeasureSearch"],[17,0,0,"-","test_Molecule"],[17,0,0,"-","test_MoleculeSet"],[17,0,0,"-","test_SimilarityMeasure"],[17,0,0,"-","test_SimilarityMeasureValueErrors"],[17,0,0,"-","test_TaskManager"],[17,0,0,"-","test_multithreading"]]},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","exception","Python exception"],"4":["py","function","Python function"],"5":["py","attribute","Python attribute"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:exception","4":"py:function","5":"py:attribute"},terms:{"0":[1,3,4,17],"01":3,"1":[1,4,5,6,17],"10":[5,6,17],"1002":5,"1021":5,"1038":5,"11":[6,17],"12":6,"13":6,"14":6,"140":5,"15":6,"16":6,"1669":5,"17":6,"18":6,"19":6,"2":[4,5,6,17],"20":[4,6],"2005":5,"2009":5,"2011":5,"2013":5,"2018":5,"2020":5,"21":6,"22":6,"23":6,"24":[4,6],"25":6,"26":6,"27":6,"28":[5,6],"29":6,"2nd":5,"3":[5,6,17],"30":6,"31":6,"32":6,"33":6,"34":6,"35":6,"36":6,"37":6,"38":6,"39":6,"4":[5,6,17],"40":6,"41":6,"42":[1,6],"43":6,"44":[5,6],"45":6,"46":6,"47":6,"5":[5,6,17],"53":5,"597":5,"6":[5,6,17],"601":5,"7":[5,6,17],"8":[1,5,6,17],"8781":5,"8787":5,"8b04532":5,"9":[6,17],"abstract":[1,3],"case":[1,4,5,17],"class":[0,1,2,3,17],"default":[1,2,3,4,17],"do":[5,17],"float":[1,3],"function":[4,17],"int":[1,2,3,4],"new":5,"return":[1,2,3,4,17],"static":[1,2],"throw":17,"true":[1,2,3],"try":[1,5,17],A:[1,5],AND:5,AS:5,BE:5,BUT:5,Be:5,FOR:5,For:5,IN:5,IS:5,If:[1,3,4,5,8],In:5,NO:5,NOT:5,OF:5,OR:5,THE:5,TO:5,The:[1,2,3,5],There:5,To:[4,5],WITH:5,__init__:5,_build:5,_can_:2,_fingerprint:2,abc:3,abil:17,abl:17,about:5,abov:5,absenc:1,absolut:3,accord:5,account:5,across:5,action:5,activ:5,addit:[1,5],addition:5,against:5,aggress:3,aimsim:[8,17],aimsim_ui_main:[8,10],aka:2,al:3,algorithm:[1,3,5,17],alias:6,all:[1,2,3,5,17],allow:17,along:[4,5],alreadi:[5,17],also:5,alt:5,altern:5,although:3,am:5,an:[0,1,3,5,8,17],analysi:[1,17],ani:5,annot:4,anoth:[1,5],apidoc:5,appar:5,apparatu:5,appear:5,applic:5,approach:17,appropri:[3,5],ar:[1,2,3,4,5,17],arbitrari:[1,2,5,17],arbitrary_descriptor_v:[1,2],arg:[1,2,3,4,17],argument:[1,2,4],aris:5,arrai:[1,2,4,17],assess:5,associ:[1,5],atom_pair:4,attribut:[1,17],attributeerror:0,austin:6,author:5,autom:5,automat:17,avail:5,avalon:4,averag:5,avoid:5,axi:4,b:[1,17],back:2,badge_logo:5,bar:4,baroni:6,base:[0,1,2,3,5,17],basic:17,becaus:1,becom:5,befor:17,behavior:17,being:[1,2],below:5,best:3,better:3,between:[1,2,3,5],bhattacharje:5,binari:[2,5],binder:5,bit:[2,17],blanquet:6,boil:1,bool:[1,2,3,4],borg:5,both:3,branch:5,braun:6,breviti:3,broken:1,browser:5,build:5,built:5,bump:5,burn:5,buser:6,c1:17,c:[5,17],calcul:[0,1,3],call:[0,2,3,5,8],campaign:5,can:[3,4,5,17],cannot:[0,17],carri:3,categori:4,cc1:17,cc:17,ccbmlib:5,ccbmlib_fingerprint:[0,10],ccc:17,cccc:17,ccccccc:17,cdatastruct:2,ch2:17,ch3:17,ch:17,charg:5,chart:4,check:[1,2,5,17],check_init:2,chem:5,chemic:5,chemical_datastructur:[0,3,10],chemist:5,chen:5,choi:6,choic:[1,3],choos:5,chosen:[1,3,5,17],cite:7,city_block_similar:6,claim:5,classmethod:17,closest:1,cluster:[0,1,3,5,10,17],cluster_data:[0,10],cluster_grouped_mol_nam:1,clusterdata:3,clustering_method:[1,2],cn:17,co:17,code:5,coeffici:1,cohen:6,cole:6,cole_1:6,cole_2:6,collect:1,collin:5,color:4,colwel:6,combin:17,combinatori:3,command:[5,8],common:4,commonli:[1,5],compar:[1,5,17],compare_against_molecul:1,compare_target_molecul:[0,10],comparetargetmolecul:[3,17],comparison:17,complet:[5,17],complex:[2,17],compon:[5,17],comprehens:5,compris:1,comptabil:2,condit:5,config:[3,5,17],config_read:10,configur:[0,3,8,17],confirgur:17,connect:5,consid:2,consist:17,consonni:6,consum:5,contain:[2,17],content:10,context:5,contract:5,contrera:5,contributor:7,control:1,convers:5,convert:[2,3,17],copi:5,copyright:5,core:5,correl:[3,5],correspond:3,cosin:6,coupl:5,cp:5,creat:[3,5,17],creation:17,csv:17,current:2,custom:17,d:5,damag:5,data:[1,3,5],databas:[3,5,17],dataset:[1,3,5],datastruct:2,davi:5,daylight:5,deal:5,decreas:3,defin:[3,5],delet:17,demo:5,denni:6,denot:[2,17],densiti:[4,5],desciptornam:5,descriptor:[0,1,5,10,17],descriptornam:5,design:5,desir:5,detect:5,determin:1,develop:7,diagon:5,dice:[6,17],dice_2:6,dice_3:6,dict:[1,2,3,4],dictionari:[1,2],differ:[4,5],dimens:5,dimension:[5,17],directli:[5,17],directori:[5,17],discov:5,discuss:5,dispers:6,displai:1,dissimilar:[1,3,5],dist:5,distanc:[1,2,3,5,6],distribut:5,divers:5,doc:5,doe:17,doi:5,don:[1,5],dotson:6,draw:[1,17],driver:6,drug:5,due:[3,5],duplic:1,dure:1,e:[1,3],each:[1,2,4,5],ecfp:5,ed:5,effici:5,efficieni:17,effort:5,either:1,element:5,empti:[8,17],enhanc:5,enough:5,ensur:[5,17],entir:5,equal:[2,4],equival:[1,5],erron:17,error:17,essenti:5,etc:[1,4],euclidean:5,euclidean_similar:6,evalu:[3,5,17],event:5,exampl:5,excel:17,except:[3,10,17],exclud:2,execut:[5,17],exist:[5,17],experiment:[2,5],explicitbitvect:2,exploratori:5,explos:3,express:5,f:5,fail:[0,1],faith:6,fals:[3,4],featur:[2,3,5,17],feature_arr:17,field:[3,8],file:[1,5,8,17],filenam:5,filetyp:17,find:[2,5,17],fingerprint1:2,fingerprint2:2,fingerprint:[1,2,3,17],fingerprint_param:[1,2],fingerprint_typ:[1,2,3,17],first:[1,4],fit:[2,5],fix:3,fixtur:17,fold:[2,17],fold_to_equal_length:2,fold_to_length:2,follow:5,fontsiz:4,forb:6,forest:5,form:[3,5],format:2,fossum:6,fp:[2,4],fpath:1,fraction:[1,3],free:5,friedman:5,from:[1,2,3,5,8,17],ftype:17,full:5,functionailti:17,furnish:5,further:5,furthest:[3,5],furthest_neighbor_correl:3,g:1,gener:[1,5],generate_fingerprint:4,generate_similarity_matrix:1,get:[1,2,3,17],get_all_supported_descriptor:2,get_best_measur:3,get_cluster_label:1,get_compatible_metr:[2,17],get_descriptor_v:1,get_distance_matrix:1,get_folded_fprint:2,get_hits_dissimilar_to:3,get_hits_similar_to:3,get_label:2,get_mol_nam:1,get_mol_properti:1,get_mol_property_v:1,get_molecule_least_similar_to:17,get_most_dissimilar_pair:[1,17],get_most_similar_pair:[1,17],get_nam:1,get_pairwise_similar:1,get_param:2,get_property_correlations_in_most_dissimilar:3,get_property_correlations_in_most_similar:3,get_property_of_most_dissimilar:1,get_property_of_most_similar:1,get_similarity_matrix:1,get_similarity_to:1,get_supported_binary_metr:2,get_supported_descriptor:2,get_supported_fprint:2,get_supported_general_metr:2,get_supported_metr:2,get_transformed_descriptor:1,get_uniq_metr:2,gh:5,github:5,give:5,gleason:6,gloriu:5,goldberg:6,good:5,goodman:6,goodman_krusk:6,grant:5,graph:[1,2,17],graphic:5,grid:4,groenen:5,group:5,ha:1,halid:5,harri:6,hash_parameter_set:4,hashed_atom_pair:4,hashed_morgan:4,hashed_tors:4,hasti:5,have:[1,3],hawkin:6,he:3,heatmap:[4,5],height:4,help:5,helper:17,herebi:5,heron:6,heteratom:5,hierarch:5,high:5,highest:3,himaghna:5,holder:5,holidai:6,holiday_denni:6,holiday_fossum:6,hook:17,hour:5,how:1,html:5,http:5,i:[1,3,5],id:[1,3],idea:5,ideal:17,ident:17,identif:17,identifi:[1,3,5],identify_outli:[0,10],identifyoutli:3,imag:[1,5],implement:[1,2,3,17],impli:5,in_dtyp:2,includ:5,index:[1,7],indic:[1,3,4,5],infer:5,inform:[1,5],initi:[0,17],input:[2,4,5,6,8,17],input_matrix:4,instal:7,instant:17,instanti:17,instead:5,interest:[3,5],interfac:[5,7,10],invalid:[0,17],invalidconfigurationerror:[0,2,4],invok:2,io:1,ioerror:8,ipynb:5,is_distance_metr:2,is_fingerprint:2,is_pres:1,is_sam:1,is_verbos:1,isol:5,isolationforest:3,issu:5,iter:5,its:[3,5],itself:17,j:5,jac:5,jaccard:6,jackson:5,just:4,k:5,keep:1,kei:1,keyword:[1,2,4],kind:5,knowl:5,kroeber:6,kruskal:6,kulczynski:6,kwarg:[1,2,3,4],l0:[5,17],l0_similar:6,l1:5,l1_similar:6,l2:5,l2_similar:6,lab:5,label:[1,2,3,4,17],label_:2,labori:5,labpath:5,lahei:6,lead:5,learn:5,least:[1,17],legend:4,legend_label:4,length:[2,17],less:4,level:1,liabil:5,liabl:5,librari:5,licens:7,limit:5,line:[5,8],linkag:5,linkedin:5,list:[1,2,3,4,5,17],load:[0,17],loadingerror:[0,17],log:17,longer:2,look:3,m2r:5,m:5,maccs_kei:4,machin:5,made:5,mai:1,main:8,make:[2,5],make_fingerprint:2,manhattan_similar:6,mani:5,manipul:1,manual:[2,5],master:5,match:17,match_fingerprint_from:1,matric:17,matrix:[1,2,4,17],max:3,max_min:3,maxim:[3,5],maximum:17,maxwel:6,md:[5,17],measur:[1,2,3,5,17],measure_search:[0,10],measuresearch:[3,17],medoid:5,merchant:5,merg:5,messag:0,method:[1,2,17],method_:1,methodnam:17,metric:[1,2,3,5,7,17],michael:6,michen:6,might:5,min:3,mine:5,minim:[3,5],minimum:17,miss:17,mit:5,model:[2,5],modern:5,modifi:[1,2,4,5],modul:[7,10],moieti:5,mol:[1,4,17],mol_descriptor_v:1,mol_graph:1,mol_property_v:1,mol_smil:[1,17],mol_src:[1,17],mol_suppl:4,mol_text:1,molecul:[0,2,3,5,10,17],molecular:[1,2,5,17],molecule_databas:1,molecule_database_src:1,molecule_database_src_typ:1,molecule_graph:2,molecule_set:[0,3,10],molecule_set_config:3,moleculeset:[1,3,17],moleculset:17,mordr:[0,5,17],mordredcalculatorerror:0,more:[3,4,5,17],morgan:[4,5,17],most:[1,3,5,17],mountford:6,much:1,multi:5,multidimension:5,multipl:[1,3,4],multiplear:4,multiprocess:[5,17],multithread:17,murrai:5,murtagh:5,mv:5,mybind:5,n:[4,17],n_bar:4,n_bars_per_xtick:4,n_cluster:[1,2],n_densiti:4,n_mol:1,n_points_per_dens:4,n_thread:1,n_xtick:4,name:[1,4,6,17],name_seq:17,namedtupl:3,natur:5,nchem:5,ndarrai:[1,2,3,4,17],nearest:[3,5],nearest_neighbor_correl:3,need:[3,5],neighbor:[3,5],newli:5,nh:17,non:[1,17],none:[0,1,2,3,4,17],noninfring:5,norm:[5,17],note:[1,2,7],notic:5,notinitializederror:[0,1,17],novel:5,np:[1,2,3,4,17],num_hit:3,number:[1,2,4,5],numpi:[1,2,4,17],numpy_:2,o:[5,17],object:[0,1,2,3,17],obtain:5,ochiai:6,often:5,oh:17,one:[1,2,4,5],ones:[4,5],onli:[2,3,17],onlin:5,only_metr:3,op:[0,1,10],open:5,oper:5,optim:[3,5,17],optim_algo:3,option:[3,4,17],order:3,org:5,oserror:0,other:[1,2,5,17],otherwis:[5,17],our:5,out:[3,5],outlier:[3,5],outlier_idx:4,output:[0,5,17],over:[3,5],overal:3,overview:5,p:5,packag:[5,7,10],padelpi:17,pair:[1,5,17],pairwis:[1,5],par:4,paramet:[0,1,2,3],parent:3,pariti:4,particular:5,partner:5,pass:[1,4,17],passthrough:17,path:[1,17],pattern:5,pca:1,pdb:17,pearson:6,pearson_heron:6,peirc:6,peirce_1:6,peirce_2:6,per:4,perform:3,permiss:5,permit:5,person:5,pharmocolog:5,pillin:6,pip:5,plot:[1,2,3,4,5],plot_barchart:4,plot_dens:4,plot_heatmap:4,plot_multiple_barchart:4,plot_par:4,plot_scatt:4,plot_titl:4,plot_title_fonts:4,plotting_script:[0,10],point:1,portion:5,potenti:5,practic:5,predict:[2,5],present:1,princip:17,probabl:5,process:17,produc:17,project:5,proper:0,properti:[0,1,3,5,17],property_seq:17,propos:5,provid:5,publish:5,pull:5,purpos:[2,7],push:5,py:[0,5],pypi:5,pyplot:4,python:[5,17],qoi:5,qualiti:5,quantiti:3,queri:[1,3],query_molecul:[1,3],r:5,rais:[1,2,4,8,17],rand:6,randomli:[1,17],rao:6,rapid:5,rare:2,rdkit:[1,2,5],rdkit_:2,rdkit_fingerprint:4,reaction:5,read:[8,17],readm:7,realiti:5,recommend:3,reduct:17,redund:[2,5],refer:[1,5],reference_mol:1,region:5,relat:5,relev:1,remov:2,repertoir:5,replic:5,repres:[2,4],represent:[1,2],request:5,requir:5,research:5,respect:1,respons:[1,3,17],restrict:5,result:5,retriev:17,right:5,robust:5,roger:6,rogot:6,rst:5,run:[7,17],runtest:17,runtimeerror:0,russel:6,s:[1,2,4,5,17],same:[1,5,17],sampl:[1,4],sample_ratio:3,sampling_random_st:1,sampling_ratio:1,satisfi:3,scalar:17,scale:5,scatter:4,scheme:5,scope:5,score:[1,3],score_:3,screen:5,search:[1,5,17],second:[1,4],see:[1,5],see_property_variation_with_similar:[0,10],seepropertyvariationwithsimilar:3,select:[1,3,5],self:[1,3],sell:5,separ:[3,5],sequenc:[3,17],seri:[4,5],serial:17,set:[1,2,3,4,5,17],set_descriptor:1,set_manu:2,set_molecul:3,set_similar:1,setup:[7,10],setupclass:17,sever:5,shade:4,shall:5,shape:4,shortcom:5,shorten:2,shorten_label:2,should:[5,17],show_plot:4,show_top:[3,17],shown:5,similar:[1,2,3,4,7,17],similarity_matrix:1,similarity_measur:[0,1,3,10,17],similarity_scor:1,similaritymeasur:[1,2,17],simple_match:6,simpson:6,sinc:[1,3],singl:[5,17],site:5,size:[2,4],smaller:2,smart:17,smarts_seq_to_smiles_fil:17,smi:17,smile:17,smiles_seq_to_pdb_dir:17,smiles_seq_to_smi_fil:17,smiles_seq_to_smiles_fil:17,smiles_seq_to_textfil:17,smiles_seq_to_xl_or_csv:17,snake_similar:6,sneath:6,sneath_1:6,sneath_2:6,sneath_3:6,sneath_4:6,so:[5,17],soc:5,softwar:5,sokal:6,solvent:5,some:[1,4],sorenson:6,sorgenfrei:6,sort:3,sorted_similar:3,sourc:1,source_molecul:1,speci:5,specifi:[1,2,5,17],specifii:5,speedup:[5,17],spend:5,sphinx:5,springer:5,start:5,state:2,statist:5,step:5,stop:17,store:[1,17],str:[1,2,3,4,17],strategi:[2,3],string:[1,2,17],structur:5,studi:1,subclass:3,subject:5,sublicens:5,submodul:10,subpackag:10,subsampl:[3,17],subsample_subset_s:3,substanti:5,substitut:5,substrat:5,sulfon:5,sulfonamid:5,suppli:[1,2,3,4],support:[0,7],sure:5,susbtrat:5,svg:5,symmetr:6,symmetric_sokal_sneath:6,synthes:5,synthesi:5,t:[1,5],tag:[2,5],take:5,tanimoto:[6,17],target:[1,5],target_mol:1,target_molecul:1,task:[0,5,8,10,17],task_manag:[0,10],taskmanag:[3,17],taxicab_similar:6,teardownclass:17,temporari:17,term:5,termin:5,test:[5,7,10],test_all_supported_measur:17,test_bad_descriptors_padelpy_descriptor:17,test_binary_only_metr:17,test_clustering_fingerprint:17,test_comparetargetmolecul:10,test_compatible_metr:17,test_descriptor:10,test_descriptor_arbitrary_list_init:17,test_descriptor_arbitrary_numpy_init:17,test_descriptor_empty_init:17,test_descriptor_make_fingerprint:17,test_empty_fprint:17,test_error_optim_algo:17,test_fingerprint_fold:17,test_fixed_fprint:17,test_fixed_similaritymeasur:17,test_get_abcd:17,test_get_molecule_least_similar_to:17,test_get_molecule_most_similar_to:17,test_get_most_dissimilar_pair:17,test_get_most_similar_pair:17,test_get_nam:17,test_get_property_valu:17,test_invalid_metr:17,test_invalid_pdb:17,test_invalid_smil:17,test_invalid_transform_error:17,test_is_sam:17,test_loadingerrorexcept:10,test_logfile_gener:17,test_match_fprint_error:17,test_max_optim_algo:17,test_mds_transform:17,test_measuresearch:10,test_min_optim_algo:17,test_missing_pdb:17,test_missing_smil:17,test_mol_mol_similarity_w_morgan_tanimoto:17,test_mol_smiles_loadingerror:17,test_mol_src_pdb_loadingerror:17,test_mol_src_txt_loadingerror:17,test_molecul:10,test_molecule_created_w_attribut:17,test_molecule_created_with_no_attribut:17,test_molecule_draw:17,test_molecule_graph_similar_to_itself_morgan_dic:17,test_molecule_graph_similar_to_itself_morgan_l0:17,test_molecule_graph_similar_to_itself_morgan_tanimoto:17,test_molecule_set_gett:17,test_molecule_set_sim_gett:17,test_moleculeset:10,test_mordred_descriptor:17,test_msearch_complet:17,test_msearch_init:17,test_msearch_init_error:17,test_multithread:10,test_multithreading_autoconfig:17,test_multithreading_consistency_10_thread:17,test_multithreading_consistency_2_thread:17,test_multithreading_consistency_3_thread:17,test_multithreading_consistency_4_thread:17,test_multithreading_consistency_5_thread:17,test_multithreading_consistency_6_thread:17,test_multithreading_consistency_7_thread:17,test_no_tasks_task_manag:17,test_nonexistent_mordred_descriptor:17,test_only_metric_fixed_fprint_search:17,test_only_metric_fixed_measure_search:17,test_only_metric_search:17,test_padelpy_descriptor:17,test_pca_transform:17,test_set_molecule_database_fingerprint_from_csv:17,test_set_molecule_database_from_csv:17,test_set_molecule_database_from_excel:17,test_set_molecule_database_from_pdb_dir:17,test_set_molecule_database_from_smarts_fil:17,test_set_molecule_database_from_smi_fil:17,test_set_molecule_database_from_smiles_fil:17,test_set_molecule_database_from_textfil:17,test_set_molecule_database_w_descriptor_property_from_csv:17,test_set_molecule_database_w_descriptor_property_from_excel:17,test_set_molecule_database_w_fingerprint_similarity_from_csv:17,test_set_molecule_database_w_property_from_csv:17,test_set_molecule_database_w_property_from_excel:17,test_set_molecule_database_w_property_from_textfil:17,test_set_molecule_database_w_similarity_from_csv:17,test_set_molecule_from_fil:17,test_set_molecule_from_smil:17,test_similarity_measure_limit:17,test_similaritymeasur:10,test_similaritymeasurevalueerror:10,test_smart:17,test_smil:17,test_speedup_efficiency_cosin:17,test_speedup_efficiency_tanimoto:17,test_subsample_molecule_database_from_csv:17,test_subsample_molecule_database_from_excel:17,test_subsample_molecule_database_from_pdb_dir:17,test_subsample_molecule_database_from_textfil:17,test_task_manag:17,test_taskmanag:10,test_topological_fprint_min_path_lesser_than_atom:17,test_tsne_transform:17,test_vectornorm_length_error:17,test_verbose_output:17,testcas:17,testcomparetargetmolecul:17,testdescriptor:17,testloadingerrorexcept:17,testmeasuresearch:17,testmolecul:17,testmoleculeset:17,testmultithread:17,testsimilaritymeasur:17,testsimilaritymeasurevalueerror:17,testtaskmanag:17,text:[1,5,17],textfil:17,than:[4,5],theori:5,therebi:5,therefor:2,thi:[1,2,3,4,5,17],third:4,though:17,thread:17,three:5,through:[5,17],thu:5,ti:1,tibshirani:5,time:[5,17],titl:4,tkinter:1,to_key_val_str:4,to_numpi:2,to_rdkit:2,todeschini:6,todeschini_1:6,todeschini_2:6,todeschini_3:6,todeschini_4:6,todeschini_5:6,toler:5,too:5,tool:5,top:3,topolog:5,torsion:4,tort:5,train:5,transform:[5,17],transit:1,tsne:17,tupl:1,tutori:7,twine:5,two:[1,2,5,17],type:[0,3,4,17],typeerror:17,typic:1,ui:[2,8,10],uintsparseintvec:2,un:[1,5],under:5,unimpl:17,uniniti:1,uniqu:2,unit:17,unittest:[5,17],unseen:5,unsupervis:17,up:17,upload:5,urbani:6,us:[0,1,2,3,4,5,17],user:[2,5],util:[0,10],v2:5,valu:[1,2,3,4,5,17],valueerror:[0,1,17],variat:5,vector:[1,2,4,17],verbos:17,verif:5,verifi:[5,17],version:5,via:[3,5],view:5,virtual:5,visual:[3,5],visualize_dataset:[0,10],visualizedataset:3,vlacho:5,vlachosgroup:5,vs:4,w:17,ward:5,warranti:5,watson:5,we:5,welcom:5,well:5,when:[0,3,5,17],where:5,whether:5,which:[1,2,3,4,5,17],whom:5,why:5,widm:5,willi:5,window:1,wire:5,without:[0,5],word:1,work:[7,17],x:[1,2,4],xlabel:4,xlabel_fonts:4,xtick:4,xtick_label:4,y:[4,5],yaml:5,ye:6,yield:5,ylabel:4,ylabel_fonts:4,your:5,yule:6,yule_1:6,yule_2:6},titles:["AIMSim package","AIMSim.chemical_datastructures package","AIMSim.ops package","AIMSim.tasks package","AIMSim.utils package","AIMSim README","Supported Similarity Metrics","AIMSim documentation","interfaces package","interfaces.UI package","AIMSim","molSim.chemical_datastructures package","molSim.ops package","molSim.tasks package","molSim.utils package","setup module","test module","tests package"],titleterms:{"function":5,aimsim:[0,1,2,3,4,5,7,10],aimsim_ui_main:9,ccbmlib_fingerprint:[4,14],chemical_datastructur:[1,11],cite:5,cluster:[2,12],cluster_data:[3,13],compare_target_molecul:[3,13],config_read:8,content:[0,1,2,3,4,7,8,9,11,12,13,14,17],contributor:5,current:5,descriptor:[2,12],develop:5,document:[5,7],except:0,fingerprint:5,identify_outli:[3,13],implement:5,indic:7,instal:5,interfac:[8,9],licens:5,measure_search:[3,13],metric:6,modul:[0,1,2,3,4,8,9,11,12,13,14,15,16,17],molecul:[1,11],molecule_set:[1,11],molsim:[11,12,13,14],note:5,op:[2,12],output:2,packag:[0,1,2,3,4,8,9,11,12,13,14,17],plotting_script:[4,14],purpos:5,readm:5,run:5,score:5,see_property_variation_with_similar:[3,13],setup:15,similar:[5,6],similarity_measur:[2,12],submodul:[0,1,2,3,4,8,9,11,12,13,14,17],subpackag:[0,8],support:[2,6],tabl:7,task:[3,13],task_manag:[3,13],test:[16,17],test_comparetargetmolecul:17,test_descriptor:17,test_loadingerrorexcept:17,test_measuresearch:17,test_molecul:17,test_moleculeset:17,test_multithread:17,test_similaritymeasur:17,test_similaritymeasurevalueerror:17,test_taskmanag:17,tutori:5,type:2,ui:9,util:[4,14],visualize_dataset:[3,13],work:5}})