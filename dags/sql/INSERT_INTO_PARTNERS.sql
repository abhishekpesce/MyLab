INSERT INTO partners (partner_name,partner_status)
VALUES ('A',TURE)
ON CONFLICT (partner_name)
DO NOTHING;
INSERT INTO partners (partner_name,partner_status)
VALUES ('B',TURE)
ON CONFLICT (partner_name)
DO NOTHING;
INSERT INTO partners (partner_name,partner_status)
VALUES ('C',TURE)
ON CONFLICT (partner_name)
DO NOTHING;