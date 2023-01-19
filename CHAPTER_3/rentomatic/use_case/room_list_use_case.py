from rentomatic.response_object.success_response_builder import SuccessResponseBuilder
from rentomatic.response_object.failed_response_builder import FailureResponseBuilder
from rentomatic.request_exceptions.invalid_room_list_request_exception import InvalidRoomListRequestException

class RoomListUseCase():
    
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        """
        Check if request is valid before calling repo list
        """
        if request.has_error():
            return FailureResponseBuilder()\
                    .build_parameters_error(request.show_clean_errors_message())

        """
        Inject valid filter request in repo
        and handle any generic errors
        """
        try:
            rooms = self.repo.list(filters=request.filters)
        except Exception as exp:
            return FailureResponseBuilder()\
                    .build_system_error(exp)
        
        """
        Build success response after validation
        """
        response = SuccessResponseBuilder()\
                    .set_value(rooms)\
                    .set_response_message_and_build('Rooms data')
        
        """
        Return success response object
        """
        return response