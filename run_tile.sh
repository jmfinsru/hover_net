python run_infer.py \
--gpu='0,1' \
--nr_types=6 \
--type_info_path=type_info.json \
--batch_size=64 \
--model_mode=fast \
--model_path=/media/jenny/PRIVATE_USB/Hover_net_files/Pannuke_checkpoints/hovernet_fast_pannuke_type_tf2pytorch.tar \
--nr_inference_workers=1 \
--nr_post_proc_workers=1 \
tile \
--input_dir=/media/jenny/PRIVATE_USB/MM_Andregangsstudiet_HE_20x_JPEG/HE_MM009_2_270125.vsi.Collection/HE_MM009_2_270125_20x_BF_01/HE_MM009_2_270125_20x_BF_01.jpg \
--output_dir=/media/jenny/PRIVATE_USB/Hover_net_files/Output/Tile \
--mem_usage=0.1 \
--draw_dot \
--save_qupath

