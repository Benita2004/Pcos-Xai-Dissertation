# dashboard/utils/input_processor.py

import pandas as pd


# Exact feature order used during model training AFTER removing ID columns
TRAINING_FEATURES = [
    'Age (yrs)',
    'Weight (Kg)',
    'Height(Cm)',
    'BMI',
    'Blood Group',
    'Pulse rate(bpm)',
    'RR (breaths/min)',
    'Hb(g/dl)',
    'Cycle(R/I)',
    'Cycle length(days)',
    'Marraige Status (Yrs)',
    'Pregnant(Y/N)',
    'No. of abortions',
    'I   beta-HCG(mIU/mL)',
    'II    beta-HCG(mIU/mL)',
    'FSH(mIU/mL)',
    'LH(mIU/mL)',
    'FSH/LH',
    'Hip(inch)',
    'Waist(inch)',
    'Waist:Hip Ratio',
    'TSH (mIU/L)',
    'AMH(ng/mL)',
    'PRL(ng/mL)',
    'Vit D3 (ng/mL)',
    'PRG(ng/mL)',
    'RBS(mg/dl)',
    'Weight gain(Y/N)',
    'hair growth(Y/N)',
    'Skin darkening (Y/N)',
    'Hair loss(Y/N)',
    'Pimples(Y/N)',
    'Fast food (Y/N)',
    'Reg.Exercise(Y/N)',
    'BP _Systolic (mmHg)',
    'BP _Diastolic (mmHg)',
    'Follicle No. (L)',
    'Follicle No. (R)',
    'Avg. F size (L) (mm)',
    'Avg. F size (R) (mm)',
    'Endometrium (mm)'
]


def prepare_input(user_inputs):
    """
    Convert sidebar inputs into the exact 41-feature format used during model training.
    """

    input_data = {
        'Age (yrs)': user_inputs.get('age', 25),
        'Weight (Kg)': user_inputs.get('weight', 60),
        'Height(Cm)': user_inputs.get('height', 160),
        'BMI': user_inputs.get('bmi', 24),
        'Blood Group': user_inputs.get('blood_group', 15),
        'Pulse rate(bpm)': user_inputs.get('pulse_rate', 72),
        'RR (breaths/min)': user_inputs.get('rr', 18),
        'Hb(g/dl)': user_inputs.get('hb', 12),
        'Cycle(R/I)': user_inputs.get('cycle_pattern', 2),
        'Cycle length(days)': user_inputs.get('cycle_length', 28),
        'Marraige Status (Yrs)': user_inputs.get('marriage_status', 0),
        'Pregnant(Y/N)': user_inputs.get('pregnant', 0),
        'No. of abortions': user_inputs.get('abortions', 0),
        'I   beta-HCG(mIU/mL)': user_inputs.get('beta_hcg_1', 1),
        'II    beta-HCG(mIU/mL)': user_inputs.get('beta_hcg_2', 1),
        'FSH(mIU/mL)': user_inputs.get('fsh', 6),
        'LH(mIU/mL)': user_inputs.get('lh', 5),
        'FSH/LH': user_inputs.get('fsh_lh', 1),
        'Hip(inch)': user_inputs.get('hip', 36),
        'Waist(inch)': user_inputs.get('waist', 30),
        'Waist:Hip Ratio': user_inputs.get('waist_hip_ratio', 0.83),
        'TSH (mIU/L)': user_inputs.get('tsh', 2),
        'AMH(ng/mL)': user_inputs.get('amh_level', 3),
        'PRL(ng/mL)': user_inputs.get('prl', 15),
        'Vit D3 (ng/mL)': user_inputs.get('vit_d3', 25),
        'PRG(ng/mL)': user_inputs.get('prg', 0.5),
        'RBS(mg/dl)': user_inputs.get('rbs', 90),
        'Weight gain(Y/N)': user_inputs.get('weight_gain', 0),
        'hair growth(Y/N)': user_inputs.get('hair_growth', 0),
        'Skin darkening (Y/N)': user_inputs.get('skin_darkening', 0),
        'Hair loss(Y/N)': user_inputs.get('hair_loss', 0),
        'Pimples(Y/N)': user_inputs.get('acne', 0),
        'Fast food (Y/N)': user_inputs.get('fast_food', 0),
        'Reg.Exercise(Y/N)': user_inputs.get('regular_exercise', 0),
        'BP _Systolic (mmHg)': user_inputs.get('bp_systolic', 120),
        'BP _Diastolic (mmHg)': user_inputs.get('bp_diastolic', 80),
        'Follicle No. (L)': user_inputs.get('follicle_count_left', user_inputs.get('follicle_count', 5)),
        'Follicle No. (R)': user_inputs.get('follicle_count_right', user_inputs.get('follicle_count', 5)),
        'Avg. F size (L) (mm)': user_inputs.get('avg_f_size_left', 15),
        'Avg. F size (R) (mm)': user_inputs.get('avg_f_size_right', 15),
        'Endometrium (mm)': user_inputs.get('endometrium', 8)
    }

    input_df = pd.DataFrame([input_data])

    # Force the exact training column order
    input_df = input_df[TRAINING_FEATURES]

    return input_df