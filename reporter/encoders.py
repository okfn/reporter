import datetime
import json
from . import formatters


class ReportJSONEncoder(json.JSONEncoder):

    """Custom JSON encoder with date handling."""

    def default(self, o):

        if isinstance(o, datetime.date):
            return o.strftime(formatters.JSON_DATE_FORMAT)

        if isinstance(o, datetime.time):
            return o.strftime(formatters.JSON_TIME_FORMAT)

        if isinstance(o, datetime.datetime):
            return o.strftime(formatters.JSON_DATETIME_FORMAT)

        return super(ReportJSONEncoder, self).default(o)
