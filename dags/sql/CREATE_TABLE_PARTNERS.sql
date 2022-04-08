create table if not exists partners (
    partner_name TEXT NOT NULL,
    partner_status BOOLEAN,
    PRIMARY KEY (partner_name)
);