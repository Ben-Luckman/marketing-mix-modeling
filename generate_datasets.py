"""
Practice Datasets for Pond Lehocky Senior Marketing Data Analyst Interview
Generated datasets cover key competencies from job description:
- Marketing Mix Modeling (MMM)
- Multi-Touch Attribution
- A/B Testing / Experiment Design
- Campaign Performance & ROI Analysis
- Customer Segmentation (Clustering)
- Lead Scoring (Predictive Modeling)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

# =============================================================================
# 1. MARKETING MIX MODELING (MMM) DATASET
# Weekly data with channel spend and business outcomes for a law firm
# =============================================================================

def generate_mmm_data():
    """
    Weekly marketing spend by channel with leads and signed cases.
    Perfect for practicing MMM, ROI analysis, and understanding channel effectiveness.
    """
    weeks = 104  # 2 years of data
    start_date = datetime(2022, 1, 3)

    data = []
    for i in range(weeks):
        week_start = start_date + timedelta(weeks=i)

        # Seasonality factors (legal services peak after holidays, accidents)
        month = week_start.month
        seasonality = 1.0 + 0.15 * np.sin(2 * np.pi * month / 12)

        # Channel spend with realistic patterns
        tv_spend = np.random.normal(25000, 5000) * (1.2 if month in [1, 9, 10] else 1.0)
        radio_spend = np.random.normal(8000, 2000)
        paid_search_spend = np.random.normal(15000, 3000)
        paid_social_spend = np.random.normal(6000, 1500)
        ooh_spend = np.random.normal(4000, 1000)  # Out of Home (billboards)
        ott_spend = np.random.normal(5000, 1500)  # Streaming TV ads
        seo_investment = np.random.normal(3000, 500)  # Ongoing SEO work

        # Ensure non-negative spend
        tv_spend = max(0, tv_spend)
        radio_spend = max(0, radio_spend)
        paid_search_spend = max(0, paid_search_spend)
        paid_social_spend = max(0, paid_social_spend)
        ooh_spend = max(0, ooh_spend)
        ott_spend = max(0, ott_spend)
        seo_investment = max(0, seo_investment)

        # Calculate leads with diminishing returns (adstock effect)
        # Each channel has different effectiveness and saturation
        tv_effect = 0.8 * np.sqrt(tv_spend / 1000)
        radio_effect = 0.4 * np.sqrt(radio_spend / 1000)
        search_effect = 1.2 * np.sqrt(paid_search_spend / 1000)
        social_effect = 0.5 * np.sqrt(paid_social_spend / 1000)
        ooh_effect = 0.3 * np.sqrt(ooh_spend / 1000)
        ott_effect = 0.6 * np.sqrt(ott_spend / 1000)
        seo_effect = 0.9 * np.sqrt(seo_investment / 1000)

        # Base leads + channel effects + seasonality + noise
        base_leads = 50
        total_effect = (tv_effect + radio_effect + search_effect +
                       social_effect + ooh_effect + ott_effect + seo_effect)
        leads = int(base_leads + total_effect * 10 * seasonality + np.random.normal(0, 8))
        leads = max(20, leads)

        # Conversion rate varies (15-25% of leads become cases)
        conversion_rate = np.random.uniform(0.15, 0.25)
        signed_cases = int(leads * conversion_rate)

        # Average case value for workers comp / personal injury
        avg_case_value = np.random.normal(8500, 2000)
        revenue = signed_cases * avg_case_value

        data.append({
            'week_start': week_start.strftime('%Y-%m-%d'),
            'tv_spend': round(tv_spend, 2),
            'radio_spend': round(radio_spend, 2),
            'paid_search_spend': round(paid_search_spend, 2),
            'paid_social_spend': round(paid_social_spend, 2),
            'ooh_spend': round(ooh_spend, 2),
            'ott_spend': round(ott_spend, 2),
            'seo_investment': round(seo_investment, 2),
            'total_spend': round(tv_spend + radio_spend + paid_search_spend +
                                paid_social_spend + ooh_spend + ott_spend + seo_investment, 2),
            'leads': leads,
            'signed_cases': signed_cases,
            'revenue': round(revenue, 2),
            'competitor_spend_index': round(np.random.uniform(80, 120), 1),
            'unemployment_rate': round(np.random.uniform(3.5, 6.0), 1)
        })

    return pd.DataFrame(data)


# =============================================================================
# 2. MULTI-TOUCH ATTRIBUTION DATASET
# Customer journey data with multiple touchpoints before conversion
# =============================================================================

def generate_attribution_data():
    """
    Individual customer journeys with multiple marketing touchpoints.
    Perfect for practicing multi-touch attribution models (first-touch, last-touch,
    linear, time-decay, position-based).
    """
    n_journeys = 2000
    channels = ['TV', 'Radio', 'Paid_Search', 'Organic_Search', 'Paid_Social',
                'Direct', 'Referral', 'OOH', 'OTT', 'Email']

    data = []
    journey_id = 1000

    for _ in range(n_journeys):
        journey_id += 1
        converted = np.random.random() < 0.18  # 18% conversion rate

        # Number of touchpoints (converted users tend to have more)
        if converted:
            n_touches = np.random.choice(range(2, 8), p=[0.1, 0.2, 0.25, 0.25, 0.15, 0.05])
        else:
            n_touches = np.random.choice(range(1, 6), p=[0.3, 0.3, 0.2, 0.15, 0.05])

        # Generate touchpoints
        start_date = datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 300))

        for touch_num in range(n_touches):
            # Channel probabilities (awareness channels early, action channels late)
            if touch_num == 0:  # First touch - awareness channels
                channel_probs = [0.25, 0.15, 0.10, 0.05, 0.15, 0.05, 0.10, 0.10, 0.05, 0.00]
            elif touch_num == n_touches - 1 and converted:  # Last touch before conversion
                channel_probs = [0.05, 0.05, 0.30, 0.20, 0.05, 0.20, 0.05, 0.02, 0.03, 0.05]
            else:  # Middle touches
                channel_probs = [0.10, 0.10, 0.20, 0.15, 0.15, 0.10, 0.08, 0.05, 0.05, 0.02]

            channel = np.random.choice(channels, p=channel_probs)
            touch_date = start_date + timedelta(days=touch_num * np.random.randint(1, 5))

            # Time spent on site varies by channel
            time_on_site = np.random.exponential(120) if channel in ['Paid_Search', 'Organic_Search', 'Direct'] else np.random.exponential(60)
            pages_viewed = max(1, int(np.random.exponential(3)))

            data.append({
                'journey_id': journey_id,
                'touchpoint_date': touch_date.strftime('%Y-%m-%d'),
                'touchpoint_order': touch_num + 1,
                'total_touchpoints': n_touches,
                'channel': channel,
                'campaign': f"{channel}_Campaign_{np.random.randint(1, 5)}",
                'device': np.random.choice(['Desktop', 'Mobile', 'Tablet'], p=[0.4, 0.5, 0.1]),
                'time_on_site_seconds': round(time_on_site, 0),
                'pages_viewed': pages_viewed,
                'form_started': 1 if np.random.random() < 0.3 else 0,
                'converted': 1 if (converted and touch_num == n_touches - 1) else 0,
                'case_type': np.random.choice(['Workers_Comp', 'Personal_Injury', 'Disability'],
                                             p=[0.5, 0.35, 0.15]) if converted else None,
                'case_value': round(np.random.normal(8500, 2500), 2) if converted else None
            })

    return pd.DataFrame(data)


# =============================================================================
# 3. A/B TESTING DATASET
# Landing page experiment data
# =============================================================================

def generate_ab_test_data():
    """
    A/B test results for landing page experiments.
    Perfect for practicing experiment design, statistical significance testing,
    and conversion rate optimization (CRO).
    """
    n_visitors = 10000

    # True conversion rates (control: 4.2%, treatment: 4.8%)
    control_rate = 0.042
    treatment_rate = 0.048

    data = []

    for i in range(n_visitors):
        visitor_id = f"V{100000 + i}"
        variant = np.random.choice(['control', 'treatment'])

        # Traffic source affects conversion
        source = np.random.choice(['Paid_Search', 'Organic', 'Social', 'Direct', 'Referral'],
                                  p=[0.35, 0.25, 0.15, 0.15, 0.10])
        source_modifier = {'Paid_Search': 1.3, 'Organic': 1.1, 'Social': 0.7,
                          'Direct': 1.2, 'Referral': 1.0}[source]

        # Device affects conversion
        device = np.random.choice(['Desktop', 'Mobile', 'Tablet'], p=[0.35, 0.55, 0.10])
        device_modifier = {'Desktop': 1.2, 'Mobile': 0.85, 'Tablet': 0.95}[device]

        # Calculate conversion probability
        base_rate = treatment_rate if variant == 'treatment' else control_rate
        conv_prob = base_rate * source_modifier * device_modifier
        converted = 1 if np.random.random() < conv_prob else 0

        # Time on page
        time_on_page = np.random.exponential(90) if converted else np.random.exponential(45)

        # Scroll depth (treatment has better engagement)
        if variant == 'treatment':
            scroll_depth = min(100, np.random.normal(72, 20))
        else:
            scroll_depth = min(100, np.random.normal(65, 22))

        data.append({
            'visitor_id': visitor_id,
            'visit_date': (datetime(2024, 6, 1) + timedelta(days=np.random.randint(0, 30))).strftime('%Y-%m-%d'),
            'variant': variant,
            'traffic_source': source,
            'device': device,
            'landing_page': 'workers_comp_lp',
            'time_on_page_seconds': round(time_on_page, 1),
            'scroll_depth_pct': round(max(0, scroll_depth), 1),
            'form_views': 1 if np.random.random() < (0.6 if variant == 'treatment' else 0.5) else 0,
            'form_starts': 1 if np.random.random() < (0.25 if variant == 'treatment' else 0.20) else 0,
            'converted': converted,
            'case_type_interest': np.random.choice(['Workers_Comp', 'Personal_Injury', 'Unknown'],
                                                   p=[0.55, 0.30, 0.15])
        })

    return pd.DataFrame(data)


# =============================================================================
# 4. CAMPAIGN PERFORMANCE & ROI DATASET
# Daily campaign metrics across channels
# =============================================================================

def generate_campaign_data():
    """
    Daily campaign performance metrics.
    Perfect for practicing ROI calculations, performance analysis, and dashboard building.
    """
    days = 180  # 6 months
    start_date = datetime(2024, 4, 1)

    campaigns = [
        {'name': 'Brand_TV_Spring', 'channel': 'TV', 'type': 'Brand', 'daily_budget': 3500},
        {'name': 'Radio_WorkersComp', 'channel': 'Radio', 'type': 'Direct_Response', 'daily_budget': 1200},
        {'name': 'Google_Search_Injury', 'channel': 'Paid_Search', 'type': 'Direct_Response', 'daily_budget': 2000},
        {'name': 'Google_Search_WorkersComp', 'channel': 'Paid_Search', 'type': 'Direct_Response', 'daily_budget': 2500},
        {'name': 'Meta_Retargeting', 'channel': 'Paid_Social', 'type': 'Retargeting', 'daily_budget': 800},
        {'name': 'Meta_Prospecting', 'channel': 'Paid_Social', 'type': 'Prospecting', 'daily_budget': 600},
        {'name': 'YouTube_PreRoll', 'channel': 'OTT', 'type': 'Brand', 'daily_budget': 700},
        {'name': 'Billboard_Highway', 'channel': 'OOH', 'type': 'Brand', 'daily_budget': 600},
    ]

    data = []

    for day_offset in range(days):
        date = start_date + timedelta(days=day_offset)
        day_of_week = date.weekday()

        # Weekend modifier (less work-related searches)
        weekend_mod = 0.7 if day_of_week >= 5 else 1.0

        for campaign in campaigns:
            # Spend varies around budget
            spend = campaign['daily_budget'] * np.random.uniform(0.85, 1.15) * weekend_mod

            # Metrics vary by channel
            if campaign['channel'] == 'Paid_Search':
                impressions = int(spend * np.random.uniform(8, 12))
                clicks = int(impressions * np.random.uniform(0.04, 0.08))
                ctr = clicks / impressions if impressions > 0 else 0
                leads = int(clicks * np.random.uniform(0.08, 0.15))
            elif campaign['channel'] == 'Paid_Social':
                impressions = int(spend * np.random.uniform(80, 120))
                clicks = int(impressions * np.random.uniform(0.008, 0.015))
                ctr = clicks / impressions if impressions > 0 else 0
                leads = int(clicks * np.random.uniform(0.03, 0.08))
            elif campaign['channel'] == 'TV':
                impressions = int(spend * np.random.uniform(15, 25))  # GRPs proxy
                clicks = 0  # No direct clicks
                ctr = 0
                leads = int(spend / 500 * np.random.uniform(0.8, 1.2))
            elif campaign['channel'] == 'Radio':
                impressions = int(spend * np.random.uniform(20, 30))
                clicks = 0
                ctr = 0
                leads = int(spend / 400 * np.random.uniform(0.7, 1.3))
            elif campaign['channel'] == 'OTT':
                impressions = int(spend * np.random.uniform(5, 10))
                clicks = int(impressions * np.random.uniform(0.005, 0.01))
                ctr = clicks / impressions if impressions > 0 else 0
                leads = int(clicks * np.random.uniform(0.05, 0.10)) + int(spend / 800)
            else:  # OOH
                impressions = int(spend * np.random.uniform(50, 80))
                clicks = 0
                ctr = 0
                leads = int(spend / 1200 * np.random.uniform(0.5, 1.5))

            # Cases from leads
            case_rate = np.random.uniform(0.12, 0.22)
            cases = int(leads * case_rate)

            # Revenue
            avg_case_value = np.random.normal(8500, 1500)
            revenue = cases * avg_case_value

            data.append({
                'date': date.strftime('%Y-%m-%d'),
                'campaign_name': campaign['name'],
                'channel': campaign['channel'],
                'campaign_type': campaign['type'],
                'spend': round(spend, 2),
                'impressions': impressions,
                'clicks': clicks,
                'ctr': round(ctr, 4),
                'leads': leads,
                'cost_per_lead': round(spend / leads, 2) if leads > 0 else 0,
                'cases': cases,
                'cost_per_case': round(spend / cases, 2) if cases > 0 else 0,
                'revenue': round(revenue, 2),
                'roas': round(revenue / spend, 2) if spend > 0 else 0
            })

    return pd.DataFrame(data)


# =============================================================================
# 5. CUSTOMER SEGMENTATION DATASET
# Lead characteristics for cluster analysis
# =============================================================================

def generate_segmentation_data():
    """
    Lead/client data with various attributes for segmentation.
    Perfect for practicing cluster analysis and customer segmentation.
    """
    n_leads = 3000

    data = []

    for i in range(n_leads):
        lead_id = f"L{200000 + i}"

        # Create distinct segments
        segment_roll = np.random.random()

        if segment_roll < 0.25:  # Segment 1: Quick converters, high value
            days_to_convert = np.random.exponential(5) + 1
            touchpoints = np.random.choice([1, 2, 3], p=[0.4, 0.4, 0.2])
            case_value = np.random.normal(12000, 2000)
            age = np.random.normal(45, 10)
            income_bracket = np.random.choice(['75k-100k', '100k-150k', '150k+'], p=[0.3, 0.4, 0.3])
            first_channel = np.random.choice(['Paid_Search', 'Direct', 'Referral'], p=[0.5, 0.3, 0.2])
        elif segment_roll < 0.50:  # Segment 2: Researchers, medium value
            days_to_convert = np.random.exponential(20) + 7
            touchpoints = np.random.choice([4, 5, 6, 7], p=[0.3, 0.3, 0.25, 0.15])
            case_value = np.random.normal(8000, 1500)
            age = np.random.normal(38, 12)
            income_bracket = np.random.choice(['50k-75k', '75k-100k', '100k-150k'], p=[0.4, 0.4, 0.2])
            first_channel = np.random.choice(['Organic_Search', 'Paid_Social', 'TV'], p=[0.5, 0.3, 0.2])
        elif segment_roll < 0.75:  # Segment 3: Price sensitive, lower value
            days_to_convert = np.random.exponential(15) + 3
            touchpoints = np.random.choice([2, 3, 4], p=[0.3, 0.4, 0.3])
            case_value = np.random.normal(5500, 1000)
            age = np.random.normal(35, 8)
            income_bracket = np.random.choice(['Under_50k', '50k-75k'], p=[0.6, 0.4])
            first_channel = np.random.choice(['Paid_Search', 'Paid_Social', 'Radio'], p=[0.4, 0.35, 0.25])
        else:  # Segment 4: Brand loyalists, high engagement
            days_to_convert = np.random.exponential(10) + 2
            touchpoints = np.random.choice([3, 4, 5], p=[0.3, 0.4, 0.3])
            case_value = np.random.normal(9500, 2000)
            age = np.random.normal(52, 12)
            income_bracket = np.random.choice(['75k-100k', '100k-150k', '150k+'], p=[0.35, 0.35, 0.3])
            first_channel = np.random.choice(['TV', 'Radio', 'Referral'], p=[0.4, 0.3, 0.3])

        # Case type
        case_type = np.random.choice(['Workers_Comp', 'Personal_Injury', 'Disability'],
                                     p=[0.50, 0.35, 0.15])

        # Geographic region (PA law firm)
        region = np.random.choice(['Philadelphia', 'Pittsburgh', 'Allentown', 'Harrisburg', 'Other_PA'],
                                  p=[0.35, 0.20, 0.15, 0.10, 0.20])

        # Engagement metrics
        website_visits = touchpoints + np.random.randint(0, 3)
        total_time_on_site = np.random.exponential(300) * touchpoints
        pages_per_visit = np.random.uniform(2, 6)
        email_opens = np.random.poisson(2)
        email_clicks = min(email_opens, np.random.poisson(1))

        data.append({
            'lead_id': lead_id,
            'acquisition_date': (datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 300))).strftime('%Y-%m-%d'),
            'first_channel': first_channel,
            'case_type': case_type,
            'region': region,
            'age': int(max(18, min(75, age))),
            'income_bracket': income_bracket,
            'days_to_convert': round(max(1, days_to_convert), 1),
            'total_touchpoints': touchpoints,
            'website_visits': website_visits,
            'total_time_on_site_mins': round(total_time_on_site / 60, 1),
            'avg_pages_per_visit': round(pages_per_visit, 1),
            'email_opens': email_opens,
            'email_clicks': email_clicks,
            'phone_calls': np.random.poisson(1),
            'case_value': round(max(2000, case_value), 2),
            'converted': 1  # All in this set converted (for segmentation of customers)
        })

    return pd.DataFrame(data)


# =============================================================================
# 6. LEAD SCORING DATASET
# Features for predictive modeling
# =============================================================================

def generate_lead_scoring_data():
    """
    Lead data with features and conversion outcome.
    Perfect for practicing predictive modeling, feature engineering, and classification.
    """
    n_leads = 5000

    data = []

    for i in range(n_leads):
        lead_id = f"LS{300000 + i}"

        # Features that influence conversion
        source = np.random.choice(['Paid_Search', 'Organic', 'TV', 'Radio', 'Social', 'Referral', 'Direct'],
                                  p=[0.25, 0.15, 0.15, 0.10, 0.12, 0.08, 0.15])
        source_score = {'Paid_Search': 0.3, 'Organic': 0.2, 'TV': 0.1, 'Radio': 0.08,
                       'Social': 0.05, 'Referral': 0.25, 'Direct': 0.22}[source]

        device = np.random.choice(['Desktop', 'Mobile', 'Tablet'], p=[0.35, 0.55, 0.10])
        device_score = {'Desktop': 0.1, 'Mobile': -0.05, 'Tablet': 0}[device]

        # Time features
        hour_of_day = np.random.randint(0, 24)
        is_business_hours = 1 if 9 <= hour_of_day <= 17 else 0
        day_of_week = np.random.randint(0, 7)
        is_weekend = 1 if day_of_week >= 5 else 0

        # Engagement features
        time_on_site = np.random.exponential(120)
        pages_viewed = max(1, int(np.random.exponential(3)))
        form_time_seconds = np.random.exponential(90) if np.random.random() < 0.6 else 0

        # Form completeness
        form_fields_filled = np.random.randint(3, 10)
        total_form_fields = 10
        form_completion_rate = form_fields_filled / total_form_fields

        # Case type
        case_type = np.random.choice(['Workers_Comp', 'Personal_Injury', 'Disability', 'Other'],
                                     p=[0.45, 0.30, 0.15, 0.10])
        case_score = {'Workers_Comp': 0.15, 'Personal_Injury': 0.12, 'Disability': 0.08, 'Other': -0.1}[case_type]

        # Previous interactions
        previous_visits = np.random.poisson(1)
        returning_visitor = 1 if previous_visits > 0 else 0

        # Calculate conversion probability
        base_prob = 0.15
        prob = base_prob + source_score + device_score + case_score
        prob += 0.05 if is_business_hours else 0
        prob += -0.03 if is_weekend else 0
        prob += 0.10 * form_completion_rate
        prob += 0.05 if returning_visitor else 0
        prob += min(0.1, time_on_site / 600)  # Capped time benefit
        prob += min(0.08, pages_viewed * 0.02)

        # Add some noise
        prob += np.random.normal(0, 0.05)
        prob = max(0.02, min(0.95, prob))

        converted = 1 if np.random.random() < prob else 0

        data.append({
            'lead_id': lead_id,
            'created_date': (datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 300))).strftime('%Y-%m-%d'),
            'source': source,
            'device': device,
            'hour_of_day': hour_of_day,
            'is_business_hours': is_business_hours,
            'day_of_week': day_of_week,
            'is_weekend': is_weekend,
            'time_on_site_seconds': round(time_on_site, 0),
            'pages_viewed': pages_viewed,
            'form_time_seconds': round(form_time_seconds, 0),
            'form_fields_filled': form_fields_filled,
            'form_completion_rate': round(form_completion_rate, 2),
            'case_type': case_type,
            'previous_visits': previous_visits,
            'returning_visitor': returning_visitor,
            'phone_provided': 1 if np.random.random() < 0.7 else 0,
            'email_provided': 1 if np.random.random() < 0.85 else 0,
            'injury_date_provided': 1 if np.random.random() < 0.5 else 0,
            'employer_provided': 1 if np.random.random() < 0.4 else 0,
            'utm_campaign': f"campaign_{np.random.randint(1, 20)}",
            'converted': converted,
            'days_to_convert': round(np.random.exponential(7) + 1, 1) if converted else None,
            'case_value': round(np.random.normal(8500, 2500), 2) if converted else None
        })

    return pd.DataFrame(data)


# =============================================================================
# GENERATE AND SAVE ALL DATASETS
# =============================================================================

if __name__ == "__main__":
    print("Generating Marketing Mix Modeling dataset...")
    mmm_df = generate_mmm_data()
    mmm_df.to_csv('01_marketing_mix_modeling.csv', index=False)
    print(f"  Saved: 01_marketing_mix_modeling.csv ({len(mmm_df)} rows)")

    print("Generating Multi-Touch Attribution dataset...")
    attribution_df = generate_attribution_data()
    attribution_df.to_csv('02_multi_touch_attribution.csv', index=False)
    print(f"  Saved: 02_multi_touch_attribution.csv ({len(attribution_df)} rows)")

    print("Generating A/B Testing dataset...")
    ab_df = generate_ab_test_data()
    ab_df.to_csv('03_ab_testing_experiment.csv', index=False)
    print(f"  Saved: 03_ab_testing_experiment.csv ({len(ab_df)} rows)")

    print("Generating Campaign Performance dataset...")
    campaign_df = generate_campaign_data()
    campaign_df.to_csv('04_campaign_performance.csv', index=False)
    print(f"  Saved: 04_campaign_performance.csv ({len(campaign_df)} rows)")

    print("Generating Customer Segmentation dataset...")
    segment_df = generate_segmentation_data()
    segment_df.to_csv('05_customer_segmentation.csv', index=False)
    print(f"  Saved: 05_customer_segmentation.csv ({len(segment_df)} rows)")

    print("Generating Lead Scoring dataset...")
    lead_df = generate_lead_scoring_data()
    lead_df.to_csv('06_lead_scoring.csv', index=False)
    print(f"  Saved: 06_lead_scoring.csv ({len(lead_df)} rows)")

    print("\nAll datasets generated successfully!")
    print("\nDataset Summary:")
    print("-" * 60)
    print("1. Marketing Mix Modeling - Weekly channel spend vs outcomes")
    print("2. Multi-Touch Attribution - Customer journey touchpoints")
    print("3. A/B Testing - Landing page experiment results")
    print("4. Campaign Performance - Daily metrics for ROI analysis")
    print("5. Customer Segmentation - Lead attributes for clustering")
    print("6. Lead Scoring - Features for predictive modeling")
