-- drop table public.endemic_vascular_occurrences cascade;
create table public.endemic_vascular_occurrences AS
with endemic_species as (
    select "speciesKey", "species", count(distinct "countryCode") number_country_codes
    from public.occurrence
    group by 1, 2
    having count(distinct "countryCode") = 1
)
select distinct occurrence."speciesKey", occurrence.species, "countryCode"
from public.occurrence
         inner join endemic_species on occurrence."speciesKey" = endemic_species."speciesKey"
;