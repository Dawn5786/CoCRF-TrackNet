# from pytracking.evaluation.environment import EnvSettings
from trackprocess.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.got10k_path = ''
    settings.lasot_path = ''
    settings.network_path = '/data1/lxt/2021remote_tracking_code/demo/trackprocess/networks/'    # Where tracking networks are stored.
    settings.nfs_path = ''
    settings.otb_path = ''
    settings.otb_path = '/data1/lxt/rssrai2019_object_tracking'
    settings.visual_path = '/data1/lxt/2021remote_tracking_code/demo/trackprocess/visual'
    settings.results_path = '/data1/lxt/2021remote_tracking_code/demo/trackprocess/tracking_results/'    # Where to store tracking results
    settings.tpl_path = ''
    settings.trackingnet_path = ''
    settings.uav_path = ''
    settings.ipiu_path = '/data1/lxt/yaogan/crop_1.25'
    settings.uav_part_path = '/data1/lxt/yaogan/test_uav_select'

    return settings

