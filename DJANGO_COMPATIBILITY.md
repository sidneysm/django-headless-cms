# Django Compatibility

## Supported Django Versions

Django Headless CMS supports Django versions from 4.0 to 5.2+.

### Version Matrix

| Django Version | Python 3.9 | Python 3.10 | Python 3.11 | Python 3.12 | Python 3.13 |
|----------------|-------------|--------------|--------------|--------------|--------------|
| 4.2 LTS        | ✅          | ✅           | ✅           | ✅           | ✅           |
| 5.0            | ✅          | ✅           | ✅           | ✅           | ✅           |
| 5.1            | ✅          | ✅           | ✅           | ✅           | ✅           |
| 5.2            | ❌          | ✅           | ✅           | ✅           | ✅           |

> **Note**: Django 5.2+ requires Python 3.10 or higher.

## Testing

To test compatibility with different Django versions:

```bash
# Test with specific Django version
pip install "Django~=5.2.0"
python -m pytest tests/

# Or use the compatibility test script
python scripts/test_django_compatibility.py
```

## Migration Notes

### Upgrading to Django 5.2+

When upgrading to Django 5.2+, ensure:

1. **Python Version**: Use Python 3.10 or higher
2. **Dependencies**: All dependencies support Django 5.2+
3. **Testing**: Run full test suite after upgrade

### Known Issues

No known compatibility issues with Django 5.2+ at this time.

## Dependency Compatibility

Key dependencies and their Django 5.2+ compatibility:

- ✅ `django-localized-fields`: Compatible
- ✅ `django-reversion`: Compatible  
- ✅ `djangorestframework`: Compatible
- ✅ `django-admin-interface`: Compatible
- ✅ `martor`: Compatible

## Reporting Issues

If you encounter compatibility issues with Django 5.2+, please:

1. Check this document for known issues
2. Test with a minimal reproduction case
3. Report the issue on GitHub with:
   - Django version
   - Python version
   - Full error traceback
   - Minimal code to reproduce