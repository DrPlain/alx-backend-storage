-- Create index on table names on the first letter of name

CREATE INDEX idx_nmae_first ON names (name(1));
