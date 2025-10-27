from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg
from psycopg.rows import dict_row
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv('.env.dashboard')

app = Flask(__name__)
CORS(app)

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', '1.tcp.ap.ngrok.io'),
    'port': os.getenv('DB_PORT', '21039'),
    'dbname': os.getenv('DB_NAME', 'postgres'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'option88')
}

def get_db_connection():
    """Create database connection"""
    try:
        conn = psycopg.connect(**DB_CONFIG, row_factory=dict_row)
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def execute_query(query, params=None):
    """Execute query and return results"""
    try:
        conn = get_db_connection()
        if not conn:
            return None, 'Database connection failed'
        
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            data = cursor.fetchall()
        
        conn.close()
        return data, None
    except Exception as e:
        return None, str(e)

@app.route('/api/nc-list', methods=['GET'])
def get_nc_list():
    """Get list of NC values for dropdown"""
    query = """
        SELECT DISTINCT nc_5g FROM cluster_5g
        WHERE nc_5g IS NOT NULL
        ORDER BY nc_5g
    """
    
    data, error = execute_query(query)
    if error:
        return jsonify({'error': error}), 500
    
    nc_list = [row['nc_5g'] for row in data]
    nc_list.insert(0, 'All')
    
    return jsonify({'nc_list': nc_list})

@app.route('/api/availability', methods=['GET'])
def get_availability():
    """Get availability data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(avail_auto_5g) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(avail_auto_5g) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/accessibility', methods=['GET'])
def get_accessibility():
    """Get accessibility data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(da_5g) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(da_5g) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/call-drop-rate', methods=['GET'])
def get_call_drop_rate():
    """Get call drop rate data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(g5_cdr) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(g5_cdr) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/sgnb-addition', methods=['GET'])
def get_sgnb_addition():
    """Get SGNB Addition SR data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(sgnb_addition_sr) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(sgnb_addition_sr) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/traffic', methods=['GET'])
def get_traffic():
    """Get Traffic 5G data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(traffic_5g) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(traffic_5g) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/eut-vs-dl', methods=['GET'])
def get_eut_vs_dl():
    """Get EUT vs DL User Thp data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(g5_eut_bhv) AS eut_value,
                MAX(g5_userdl_thp) AS dl_value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(g5_eut_bhv) AS eut_value,
                MAX(g5_userdl_thp) AS dl_value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'eut_value': float(row['eut_value']) if row['eut_value'] else 0,
        'dl_value': float(row['dl_value']) if row['dl_value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/user-5g', methods=['GET'])
def get_user_5g():
    """Get User 5G data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(sum_en_dc_user_5g_wd) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(sum_en_dc_user_5g_wd) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/dl-prb-util', methods=['GET'])
def get_dl_prb_util():
    """Get DL PRB Utilization data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(g5_dlprb_util) * 100 AS util_value,
                MAX(dl_prb_util_5g_count_gt_085) AS count_value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(g5_dlprb_util) * 100 AS util_value,
                MAX(dl_prb_util_5g_count_gt_085) AS count_value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'util_value': float(row['util_value']) if row['util_value'] else 0,
        'count_value': float(row['count_value']) if row['count_value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/inter-esgnb', methods=['GET'])
def get_inter_esgnb():
    """Get Inter-eSgNB PSCell Change data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(inter_esgnb) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(inter_esgnb) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/intra-esgnb', methods=['GET'])
def get_intra_esgnb():
    """Get Intra-eSgNB PSCell Change data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(intra_esgnb) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(intra_esgnb) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/intra-sgnb-intrafreq', methods=['GET'])
def get_intra_sgnb_intrafreq():
    """Get Intra-SgNB Intrafreq PSCell Change data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(intra_sgnb_intrafreq) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(intra_sgnb_intrafreq) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/inter-sgnb-intrafreq', methods=['GET'])
def get_inter_sgnb_intrafreq():
    """Get Inter-SgNB Intrafreq PSCell Change data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(inter_sgnb_intrafreq) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(inter_sgnb_intrafreq) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/')
def index():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': '5G KPI Dashboard API'})

# ==================== 4G KPI ENDPOINTS ====================

@app.route('/api/4g-availability', methods=['GET'])
def get_4g_availability():
    """Get 4G availability data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(g4_avail_auto) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(g4_avail_auto) * 100 AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/4g-accessibility', methods=['GET'])
def get_4g_accessibility():
    """Get 4G accessibility (S1 Failure) data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(s1_failure) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(s1_failure) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/4g-rrc-user', methods=['GET'])
def get_4g_rrc_user():
    """Get 4G RRC User data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(rrc_ue) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(rrc_ue) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/4g-traffic', methods=['GET'])
def get_4g_traffic():
    """Get 4G Traffic data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(traffic_4g) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(traffic_4g) AS value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'value': float(row['value']) if row['value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/4g-eut', methods=['GET'])
def get_4g_eut():
    """Get 4G EUT vs EUT < 3.1mbps data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(eut_4g_bh) AS eut_value,
                MAX(eut_4g_bh_count_less_31) AS eut_less_31
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(eut_4g_bh) AS eut_value,
                MAX(eut_4g_bh_count_less_31) AS eut_less_31
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'eut_value': float(row['eut_value']) if row['eut_value'] else 0,
        'eut_less_31': float(row['eut_less_31']) if row['eut_less_31'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/4g-dl-prb-util', methods=['GET'])
def get_4g_dl_prb_util():
    """Get 4G DL PRB Utilization data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(dl_prb_util) * 100 AS util_value,
                MAX(dl_prb_util_count_gt_09) AS count_value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(dl_prb_util) * 100 AS util_value,
                MAX(dl_prb_util_count_gt_09) AS count_value
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'util_value': float(row['util_value']) if row['util_value'] else 0,
        'count_value': float(row['count_value']) if row['count_value'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/4g-cqi', methods=['GET'])
def get_4g_cqi():
    """Get 4G CQI data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(cqi_bh) AS cqi_value,
                MAX(cqi_less_than_7) AS cqi_less_7
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(cqi_bh) AS cqi_value,
                MAX(cqi_less_than_7) AS cqi_less_7
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'cqi_value': float(row['cqi_value']) if row['cqi_value'] else 0,
        'cqi_less_7': float(row['cqi_less_7']) if row['cqi_less_7'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/4g-user', methods=['GET'])
def get_4g_user():
    """Get 4G User IOH vs IM3 data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(user_ioh) AS user_ioh,
                MAX(user_im3) AS user_im3
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(user_ioh) AS user_ioh,
                MAX(user_im3) AS user_im3
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'user_ioh': float(row['user_ioh']) if row['user_ioh'] else 0,
        'user_im3': float(row['user_im3']) if row['user_im3'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/4g-traffic-comparison', methods=['GET'])
def get_4g_traffic_comparison():
    """Get 4G vs 5G Traffic comparison data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                MAX(traffic_4g) AS traffic_4g,
                MAX(traffic_5g) AS traffic_5g
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                MAX(traffic_4g) AS traffic_4g,
                MAX(traffic_5g) AS traffic_5g
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'traffic_4g': float(row['traffic_4g']) if row['traffic_4g'] else 0,
        'traffic_5g': float(row['traffic_5g']) if row['traffic_5g'] else 0
    } for row in data]
    
    return jsonify({'data': result})

@app.route('/api/4g-traffic-percent', methods=['GET'])
def get_4g_traffic_percent():
    """Get 4G vs 5G Traffic percentage data"""
    nc_selector = request.args.get('nc', 'All')
    
    if nc_selector == 'All':
        query = """
            SELECT
                date_column::date AS time,
                'All NC' AS metric,
                (MAX(traffic_4g) / NULLIF(MAX(traffic_4g) + MAX(traffic_5g), 0)) * 100 AS traffic_4g_pct,
                (MAX(traffic_5g) / NULLIF(MAX(traffic_4g) + MAX(traffic_5g), 0)) * 100 AS traffic_5g_pct
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
            GROUP BY date_column::date
            ORDER BY date_column::date
        """
        data, error = execute_query(query)
    else:
        query = """
            SELECT
                date_column::date AS time,
                nc_5g AS metric,
                (MAX(traffic_4g) / NULLIF(MAX(traffic_4g) + MAX(traffic_5g), 0)) * 100 AS traffic_4g_pct,
                (MAX(traffic_5g) / NULLIF(MAX(traffic_4g) + MAX(traffic_5g), 0)) * 100 AS traffic_5g_pct
            FROM cluster_5g
            WHERE date_column >= now() - interval '35 days'
                AND nc_5g = %s
            GROUP BY date_column::date, nc_5g
            ORDER BY date_column::date
        """
        data, error = execute_query(query, (nc_selector,))
    
    if error:
        return jsonify({'error': error}), 500
    
    result = [{
        'time': row['time'].isoformat(),
        'metric': row['metric'],
        'traffic_4g_pct': float(row['traffic_4g_pct']) if row['traffic_4g_pct'] else 0,
        'traffic_5g_pct': float(row['traffic_5g_pct']) if row['traffic_5g_pct'] else 0
    } for row in data]
    
    return jsonify({'data': result})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
