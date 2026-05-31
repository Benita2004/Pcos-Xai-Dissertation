# dashboard/utils/input_processor.py

import pandas as pd


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


def yes_no_to_number(value, field_name="This field"):
    """
    Convert Yes/No dashboard inputs into numeric values.

    Yes = 1
    No = 0
    """

    if value is None or value == "":
        return 0

    value = str(value).strip().lower()

    if value == "yes":
        return 1

    if value == "no":
        return 0

    raise ValueError(f"{field_name} must be Yes or No.")


def cycle_to_number(value):
    """
    Convert cycle pattern input into numeric training format.

    Regular = 2
    Irregular = 4
    """

    if value is None or value == "":
        return 2

    value = str(value).strip().lower()

    if value == "regular":
        return 2

    if value == "irregular":
        return 4

    raise ValueError("Cycle Pattern must be Regular or Irregular.")


def to_float(value, default_value, min_value=None, max_value=None, field_name="This field"):
    """
    Convert sidebar text input into float.

    If the field is empty, use a default value.
    If a dataset-based range is provided, validate the value.

    These validation ranges are based on the training dataset
    and are not clinical diagnostic thresholds.
    """

    if value is None or str(value).strip() == "":
        return default_value

    try:
        value = float(value)
    except ValueError:
        raise ValueError(f"{field_name} must be a number.")

    if min_value is not None and max_value is not None:
        if value < min_value or value > max_value:
            raise ValueError(f"{field_name} must be between {min_value} and {max_value}.")

    return value


def prepare_input(user_inputs):
    """
    Convert sidebar inputs into the exact 41-feature numeric format
    used during model training.

    Dataset-based validation is applied to all visible sidebar inputs.
    """

    age = to_float(
        user_inputs.get('age'),
        25,
        min_value=20,
        max_value=48,
        field_name="Age"
    )

    weight = to_float(
        user_inputs.get('weight'),
        60,
        min_value=31,
        max_value=108,
        field_name="Weight"
    )

    bmi = to_float(
        user_inputs.get('bmi'),
        24,
        min_value=12,
        max_value=39,
        field_name="BMI"
    )

    follicle_count = to_float(
        user_inputs.get('follicle_count'),
        5,
        min_value=0,
        max_value=22,
        field_name="Follicle Count"
    )

    amh_level = to_float(
        user_inputs.get('amh_level'),
        3,
        min_value=0,
        max_value=66,
        field_name="AMH Level"
    )

    cycle_pattern = cycle_to_number(
        user_inputs.get('cycle_pattern')
    )

    hair_growth = yes_no_to_number(
        user_inputs.get('hair_growth'),
        field_name="Excess Hair Growth"
    )

    skin_darkening = yes_no_to_number(
        user_inputs.get('skin_darkening'),
        field_name="Skin Darkening"
    )

    weight_gain = yes_no_to_number(
        user_inputs.get('weight_gain'),
        field_name="Weight Gain"
    )

    acne = yes_no_to_number(
        user_inputs.get('acne'),
        field_name="Acne"
    )

    input_data = {
        'Age (yrs)': age,
        'Weight (Kg)': weight,
        'Height(Cm)': to_float(user_inputs.get('height'), 160),
        'BMI': bmi,
        'Blood Group': to_float(user_inputs.get('blood_group'), 15),
        'Pulse rate(bpm)': to_float(user_inputs.get('pulse_rate'), 72),
        'RR (breaths/min)': to_float(user_inputs.get('rr'), 18),
        'Hb(g/dl)': to_float(user_inputs.get('hb'), 12),

        'Cycle(R/I)': cycle_pattern,
        'Cycle length(days)': to_float(user_inputs.get('cycle_length'), 28),

        'Marraige Status (Yrs)': to_float(user_inputs.get('marriage_status'), 0),
        'Pregnant(Y/N)': yes_no_to_number(user_inputs.get('pregnant'), field_name="Pregnant"),
        'No. of abortions': to_float(user_inputs.get('abortions'), 0),

        'I   beta-HCG(mIU/mL)': to_float(user_inputs.get('beta_hcg_1'), 1),
        'II    beta-HCG(mIU/mL)': to_float(user_inputs.get('beta_hcg_2'), 1),
        'FSH(mIU/mL)': to_float(user_inputs.get('fsh'), 6),
        'LH(mIU/mL)': to_float(user_inputs.get('lh'), 5),
        'FSH/LH': to_float(user_inputs.get('fsh_lh'), 1),

        'Hip(inch)': to_float(user_inputs.get('hip'), 36),
        'Waist(inch)': to_float(user_inputs.get('waist'), 30),
        'Waist:Hip Ratio': to_float(user_inputs.get('waist_hip_ratio'), 0.83),

        'TSH (mIU/L)': to_float(user_inputs.get('tsh'), 2),
        'AMH(ng/mL)': amh_level,
        'PRL(ng/mL)': to_float(user_inputs.get('prl'), 15),
        'Vit D3 (ng/mL)': to_float(user_inputs.get('vit_d3'), 25),
        'PRG(ng/mL)': to_float(user_inputs.get('prg'), 0.5),
        'RBS(mg/dl)': to_float(user_inputs.get('rbs'), 90),

        'Weight gain(Y/N)': weight_gain,
        'hair growth(Y/N)': hair_growth,
        'Skin darkening (Y/N)': skin_darkening,
        'Hair loss(Y/N)': yes_no_to_number(user_inputs.get('hair_loss'), field_name="Hair Loss"),
        'Pimples(Y/N)': acne,
        'Fast food (Y/N)': yes_no_to_number(user_inputs.get('fast_food'), field_name="Fast Food"),
        'Reg.Exercise(Y/N)': yes_no_to_number(user_inputs.get('regular_exercise'), field_name="Regular Exercise"),

        'BP _Systolic (mmHg)': to_float(user_inputs.get('bp_systolic'), 120),
        'BP _Diastolic (mmHg)': to_float(user_inputs.get('bp_diastolic'), 80),

        'Follicle No. (L)': follicle_count,
        'Follicle No. (R)': follicle_count,

        'Avg. F size (L) (mm)': to_float(user_inputs.get('avg_f_size_left'), 15),
        'Avg. F size (R) (mm)': to_float(user_inputs.get('avg_f_size_right'), 15),
        'Endometrium (mm)': to_float(user_inputs.get('endometrium'), 8)
    }

    input_df = pd.DataFrame([input_data])

    input_df = input_df[TRAINING_FEATURES]

    input_df = input_df.astype(float)

    return input_df