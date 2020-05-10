class ConectionsErrors(object):
    class CalcsError(Exception):
        pass

    class SQLError(Exception):
        pass

    class CreateTableError(Exception):
        pass

    class ConsultError(Exception):
        pass

    class InsertError(Exception):
        pass

    class DellError(Exception):
        pass

    class UpdatedError(Exception):
        pass
