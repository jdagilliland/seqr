from xbrowse.variant_search import utils as search_utils
from django.conf import settings
from xbrowse_server.api.utils import add_extra_info_to_variants_family, add_extra_info_to_variants_project


def get_variants_in_gene(family_group, gene_id, variant_filter=None, quality_filter=None):
    """

    """
    variants_by_family = []
    for family in family_group.get_families():
        variant_list = list(settings.DATASTORE.get_variants_in_gene(
            family.project.project_id,
            family.family_id,
            gene_id,
            variant_filter=variant_filter
        ))
        variant_list = search_utils.filter_gene_variants_by_variant_filter(variant_list, gene_id, variant_filter)
        add_extra_info_to_variants_family(settings.REFERENCE, family, variant_list)
        variants_by_family.append({
            'variants': [v.toJSON() for v in variant_list],
            'family_id': family.family_id,
            'project_id': family.project.project_id,
            'family_name': str(family),
        })
    return variants_by_family