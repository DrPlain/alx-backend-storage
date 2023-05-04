-- Lists all bands with `Glam rock` as their main style,
-- Ranked by their longevity

-- Create a view that changes NULL to 2020 in column split
CREATE OR REPLACE VIEW old_school_band AS
SELECT band_name, formed, COALESCE(split, 2020) AS split, style
FROM metal_bands;

-- Use the created view to filter required data
SELECT band_name, (split - formed) AS lifespan
FROM old_school_band
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
