import psycopg2
import pandas as pd
from datetime import datetime, timedelta

DB_CONFIG = {
    'host': '1.tcp.ap.ngrok.io',
    'port': 21039,
    'database': 'postgres',
    'user': 'postgres',
    'password': 'option88'
}

# Connect to database
conn = psycopg2.connect(**DB_CONFIG)

# Analyze cluster_5g data
print("=" * 70)
print("ANALYZING CLUSTER_5G DATA")
print("=" * 70)

# Get date range
query = "SELECT MIN(date_column), MAX(date_column) FROM cluster_5g"
df_dates = pd.read_sql(query, conn)
print("\nDate range:")
print(df_dates)

# Get recent data samples (last 30 days)
query = """
SELECT date_column, 
       COUNT(*) as record_count,
       AVG(avail_auto_5g) as avg_avail_5g,
       MAX(avail_auto_5g) as max_avail_5g,
       MIN(avail_auto_5g) as min_avail_5g,
       AVG(g4_avail_auto) as avg_avail_4g,
       MAX(g4_avail_auto) as max_avail_4g,
       MIN(g4_avail_auto) as min_avail_4g
FROM cluster_5g 
WHERE date_column >= (SELECT MAX(date_column)::date - INTERVAL '30 days' FROM cluster_5g)
GROUP BY date_column
ORDER BY date_column DESC
LIMIT 30
"""
df_recent = pd.read_sql(query, conn)
print("\n\nRecent 30 days summary:")
print(df_recent)

# Get sample of actual values
query = """
SELECT date_column,
       nc_5g,
       avail_auto_5g,
       da_5g,
       g5_cdr,
       sgnb_addition_sr,
       traffic_5g,
       g5_userdl_thp,
       sum_en_dc_user_5g_wd,
       g5_dlprb_util,
       inter_esgnb,
       intra_esgnb,
       inter_sgnb_intrafreq,
       intra_sgnb_intrafreq,
       g4_avail_auto,
       s1_failure,
       rrc_ue,
       traffic_4g,
       eut_4g_bh,
       dl_prb_util,
       cqi_bh,
       g5_cqi
FROM cluster_5g 
WHERE date_column >= (SELECT MAX(date_column)::date - INTERVAL '7 days' FROM cluster_5g)
ORDER BY date_column DESC
LIMIT 20
"""
df_sample = pd.read_sql(query, conn)
print("\n\nSample data (last 7 days):")
print(df_sample)

conn.close()
