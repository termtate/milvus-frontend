from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    ANN_SEARCH_FIELDS: tuple[str, ...] = ("发作演变过程", ) # TODO 
    COLUMNS_NAME_MAP: dict[str, str] = {
        "ID": "id",
        "身份证号": "id_card_number",
        "姓名": "name",
        "第几次住院": "hospitalize_num",
        "病案号": "case_number",
        "性别": "sex",
        "年龄": "age",
        "电话": "phone_number",
        "发作演变过程": "seizure_evolution",
        "发作持续时间": "seizure_duration",
        "发作频次": "seizure_freq",
        "母孕年龄": "maternal_pregnancy_age",
        "孕次产出": "pregnancy_num",
        "出生体重": "birth_weight",
        "头围": "head_c",
        "血、尿代谢筛查": "blood_urine_screening",
        "铜兰蛋白": "copper_cyanin",
        "脑脊液": "csf",
        "基因检查": "genetic_test",
        "头部CT": "head_ct",
        "头部MRI": "head_mri",
        "头皮脑电图": "scalp_eeg",
        "诱发因素": "precipitating_factor",
    }
    
    TABLE_COLUMNS: tuple[str, ...] = tuple(COLUMNS_NAME_MAP.keys())


settings = Settings()