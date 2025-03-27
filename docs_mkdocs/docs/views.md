# Views Documentation

## UserListView
- **Type**: `TemplateView`
- **Template**: `app/template.html`
- **Functionality**:
  - Получает данные из таблицы (ID: `m3z6v1b977wlhfm`)
  - Передает записи в контекст шаблона как `records`
- **Exception Handling**: Ловит и выводит ошибки при получении данных

## API ViewSets

### QuestionViewSet
- **Model**: `Question`
- **Serializer**: `QuestionSerializer`
- **Endpoints**: CRUD для модели Question

### ChoiceViewSet
- **Model**: `Choice`
- **Serializer**: `ChoiceSerializer`
- **Endpoints**: CRUD для модели Choice

### UserViewSet
- **Model**: `User`
- **Serializer**: `UserSerializer`
- **Endpoints**: CRUD для модели User

---

