from rest_framework.views import exception_handler


def get_response_errors(r):
    errors = []
    for field, value in r.items():
        valstr = ''
        for val in value:
            if type(val) is dict:
                for _, v in val.items():
                    valstr = valstr + ' '.join(v)
            else:
                valstr = valstr + val + ' '
        errors.append(f'{field} : {valstr.strip()}')
    return errors


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    request = context['request']
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR'].split(',')[
            0].strip()

    # Now add the HTTP status code to the response.
    if response is not None:
        errors = []
        if not isinstance(response.data, list):
            message = response.data.get('detail')
            if not message:
                error_codes = response.data.pop('error_code', None)
                if error_codes and isinstance(error_codes, list):
                    error_code = error_codes[0]
                else:
                    error_code = '01'
                errors = get_response_errors(response.data)
                response.data = {'success': False, 'error_code': error_code,
                                 'message': f'{str(exc.__class__.__name__)} ({errors})', 'data': None, 'errors': errors}
            else:
                response.data = {'success': False, 'error_code': '01',
                                 'message': message, 'data': None, 'error': ['detail : %s' % message]}
        else:
            for r in response.data:
                message = r.get('detail')
                if not message:
                    errors.extend(get_response_errors(r))
                else:
                    errors.append(
                        f'{"detail"} : {message.strip() if not isinstance(message, list) else message}')
            response.data = {'success': False, 'error_code': '01',
                             'message': f'{str(exc.__class__.__name__)} ({errors})', 'data': None, 'errors': errors}

    return response
