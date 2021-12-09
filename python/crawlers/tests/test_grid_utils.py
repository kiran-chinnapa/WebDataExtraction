from unittest import TestCase
from crawlers.utils import grid_utils


class TestGridUtils(TestCase):

    def test_global_search(self):
        test_query = '{ "query": { "selectColumnNames": ["Website URL"], ' '"pagination": {"startRow": 1,"rowCount": 1003},'\
                       '"sendRowIdsInResponse": true, "showColumnNamesInResponse": true}}'

        result =grid_utils.global_search(grid_id='58c6f4d8c097d64efa264c39/share/5cf94950c9d08233ceac2977',
                                              auth_id = 'ed0444ad-9e34-43b5-b0f5-5d08351a3def',
                                              search_query=test_query,
                                              env='prod')
        print('no of rows: {}'.format(len(result['rows'])))
        for rslt_rows in result['rows']:
            company_website = rslt_rows['Website URL']
            print('processing company : {}'.format(company_website))
        self.assertIsNotNone(rslt_rows)

    def test_read_dmv_companies(self):
        dmv_rows,start_urls =grid_utils.read_dmv_companies()
        self.assertIsNotNone(dmv_rows,start_urls)

