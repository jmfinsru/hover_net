python run_infer.py \
--gpu='0,1' \
--nr_types=6 \
--type_info_path=type_info.json \
--batch_size=16 \
--model_mode=fast \
--model_path=/media/jenny/PRIVATE_USB/Hover_net_files/Pannuke_checkpoints/hovernet_fast_pannuke_type_tf2pytorch.tar \
--nr_inference_workers=2 \
--nr_post_proc_workers=4 \
wsi \
--input_dir=/media/jenny/PRIVATE_USB/Converted_images \
--output_dir=/media/jenny/PRIVATE_USB/Hover_net_files/Output/WSI \
--input_mask_dir=/media/jenny/PRIVATE_USB/masks_test/ \
--save_thumb \
--save_mask
