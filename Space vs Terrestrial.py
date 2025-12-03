# Performance comparison
PERFORMANCE_COMPARISON = {
    'detection_range': {
        'terrestrial': {
            'small_drone': '25-35 meters',
            'vehicle': '75 meters',
            'aircraft': 'N/A (limited by horizon)',
        },
        'space_based': {
            'small_drone': '50-100 km',
            'vehicle': '500-1000 km',
            'aircraft': '500-1000 km',
            'icbm': 'Global coverage',
        },
        'improvement': {
            'small_drone': '2000-4000x',
            'vehicle': '6700-13300x',
            'aircraft': 'Infinite (terrestrial cannot detect beyond horizon)',
        }
    },
    'coverage_area': {
        'terrestrial': {
            'single_sensor': '~1 km² (for drone detection)',
            'network': '~100 km² (with 10 sensors)',
        },
        'space_based': {
            'single_satellite': '~785,000 km² (500 km altitude)',
            'constellation': '510 million km² (entire Earth surface)',
        },
        'improvement': {
            'single_sensor': '785,000x',
            'network': '5.1 millionx',
        }
    },
    'warning_time': {
        'terrestrial': {
            'hypersonic': '10-30 seconds (at detection range)',
            'cruise_missile': '1-2 minutes',
        },
        'space_based': {
            'hypersonic': '3-4 minutes',
            'cruise_missile': '25-27 minutes',
            'icbm': '25-30 minutes',
        },
        'improvement': {
            'hypersonic': '6-8x longer warning',
            'cruise_missile': '15-25x longer warning',
        }
    },
    'stealth_penetration': {
        'terrestrial': {
            'effectiveness': 'Limited by stealth shaping and materials',
            'range_reduction': '10-100x reduction against stealth',
        },
        'space_based': {
            'effectiveness': 'Quantum radar penetrates most stealth',
            'range_reduction': '2-5x reduction against stealth',
            'reason': 'Quantum entanglement correlations ignore conventional absorption',
        }
    }
}
