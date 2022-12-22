app_list =
[
    {
        'name': 'Authentication and Authorization',
        'app_label': 'auth',
        'app_url': '/admin/auth/',
        'has_module_perms': True,
        'models':
        [
            {
                'model': <class 'django.contrib.auth.models.Group'>,
                'name': 'Groups',
                'object_name': 'Group',
                'perms':
                {
                    'add': True,
                    'change': True,
                    'delete': True,
                    'view': True
                },
                'admin_url': '/admin/auth/group/',
                'add_url': '/admin/auth/group/add/',
                'view_only': False
            },
            {
                'model': <class 'django.contrib.auth.models.User'>,
                'name': 'Users',
                'object_name': 'User',
                'perms':
                {
                    'add': True,
                    'change': True,
                    'delete': True,
                    'view': True
                },
                'admin_url': '/admin/auth/user/',
                'add_url': '/admin/auth/user/add/',
                'view_only': False
            }
        ]
    },
    {
            'name': 'Config',
            'app_label': 'config',
            'app_url': '/admin/config/',
            'has_module_perms': True,
            'models':
            [
                {
                    'model': <class 'config.models.Country'>,
                    'name': 'Countries',
                    'object_name': 'Country',
                    'perms':
                    {
                        'add': True,
                        'change': True,
                        'delete': True,
                        'view': True
                    },
                    'admin_url': '/admin/config/country/',
                    'add_url': '/admin/config/country/add/',
                    'view_only': False
                },
                {
                    'model': <class 'config.models.Language'>,
                    'name': 'Languages',
                    'object_name': 'Language',
                    'perms':
                    {
                        'add': True,
                        'change': True,
                        'delete': True,
                        'view': True
                    },
                    'admin_url': '/admin/config/language/',
                    'add_url': '/admin/config/language/add/',
                    'view_only': False
                }
            ]
        },
        {
            'name': 'Course',
            'app_label': 'course',
            'app_url': '/admin/course/',
            'has_module_perms': True,
            'models':
            [
                {
                    'model': <class 'course.models.Course'>,
                    'name': 'Courses',
                    'object_name': 'Course',
                    'perms': {
                        'add': True,
                        'change': True,
                        'delete': True,
                        'view': True
                    },
                    'admin_url': '/admin/course/course/',
                    'add_url': '/admin/course/course/add/',
                    'view_only': False
                },
                {
                    'model': <class 'course.models.Level'>,
                    'name': 'Levels',
                    'object_name': 'Level',
                    'perms':
                    {
                        'add': True,
                        'change': True,
                        'delete': True,
                        'view': True
                    },
                    'admin_url': '/admin/course/level/',
                    'add_url': '/admin/course/level/add/',
                    'view_only': False
                },
                {
                    'model': <class 'course.models.Word'>,
                    'name': 'Words',
                    'object_name': 'Word',
                    'perms':
                    {
                        'add': True,
                        'change': True,
                        'delete': True,
                        'view': True},
                        'admin_url': '/admin/course/word/',
                        'add_url': '/admin/course/word/add/',
                        'view_only': False
                    }
                ]
            }
        ]
