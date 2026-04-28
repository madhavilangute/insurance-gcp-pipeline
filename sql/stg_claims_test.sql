-- Test SQL for Staging Layer
SELECT 
    claim_id,
    UPPER(policy_type) as policy_type,
    CURRENT_TIMESTAMP() as processed_at
FROM `your-project.your_dataset.raw_claims`
LIMIT 10;