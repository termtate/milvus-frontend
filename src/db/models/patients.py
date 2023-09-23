from pymilvus import CollectionSchema, DataType, FieldSchema
from common.config import settings
from db.models.table import Table 


patients = Table(
    table_name="patients1",
    fields=[
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="id_card_number", dtype=DataType.VARCHAR, max_length=1000),
        
        FieldSchema(name="hospitalize_num", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="name", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="case_number", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="sex", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="age", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="phone_number", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="seizure_evolution", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="seizure_duration", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="seizure_freq", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="maternal_pregnancy_age", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="pregnancy_num", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="birth_weight", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="head_c", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="blood_urine_screening", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="copper_cyanin", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="csf", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="genetic_test", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="head_ct", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="head_mri", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="scalp_eeg", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="precipitating_factor", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="childhood_onset", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="aed", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="epilepsy_surgery", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="simple_sensory_seizure", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="is_parent_febrile_convulsion", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="pregnancy_diseases", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="infancy_onset", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="motor_seizure", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="metabolic_disorders", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="postictal_manifestation", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="symptomatic_epilepsy", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="have_surgery_history", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="automatism", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="generalized_motor_seizures", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="pigmentation", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="local_motor_seizures", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="autonomic_nerves", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="cognition", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="other_epilepsy_syndrome", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="electrolyte", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="neonatal_onset", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="vaccination_history", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="is_relatives_have_epilepsy", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="lactate", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="growth_milestone", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="growth_retardation", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="adolescent_adult_onset", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="stunting", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="blood_ammonia", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="generalized_non_motor_seizures", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="learning_difficulties", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="focal_non_motor_seizures", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="overprotected", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="has_febrile_seizures_history", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="has_neonatal_convulsion", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="adhd", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="has_severe_jaundice", dtype=DataType.VARCHAR, max_length=1000),
    ],
    vector_fields=[
        "seizure_evolution",   
        "precipitating_factor"   
    ],
    index_params=settings.milvus.VECTOR_FIELD_INDEX_PARAMS
)