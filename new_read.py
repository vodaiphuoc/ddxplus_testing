# python code/basd/main.py --cuda_idx 0 --seed 2919 --n_workers 4 --thres 0.5 \
# --min_rec_ratio 1.0 --output "./" --run_mode "train" \
# --evi_meta_path "data/release_evidences.json" \
# --patho_meta_path "data/release_conditions.json" \
# --eval_batch_size 4139 --batch_size 2657 --num_epochs 100 --interaction_length 30 \
# --patience 20 --data "data/release_train_patients.zip" \
# --eval_data "data/release_validate_patients.zip" \
# --lr 0.0003469 --only_diff_at_end 1 --hidden_size 2048 --num_layers 3 \
# --masked_inquired_actions --include_turns_in_state --compute_metrics_flag \


import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data", help="path to the patient data file", type=str, required=True
    )
    parser.add_argument(
        "--eval_data",
        help="path to the patient data file for evaluation purposes."
        " if not set, use the data paremeter as default value.",
        type=str,
        default=None,
    )
    args = parser.parse_args()

    print(vars(args))
    print(type(vars(args)))

    with open('args.json','w') as fp:
        json.dump(vars(args), fp, indent=4)

if __name__ == '__main__':
    main()