from django.contrib import admin
from seqr.models import Project, Family, Individual, SequencingSample, Dataset, \
    LocusList, LocusListEntry, \
    VariantNote, VariantTag, VariantTagType

for m in [Project, Family, Individual, SequencingSample, Dataset,
            LocusList, LocusListEntry,
            VariantNote, VariantTag, VariantTagType]:
    admin.site.register(m)