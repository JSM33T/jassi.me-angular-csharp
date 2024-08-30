using Jassi.Entities.DTO;
using Jassi.Entities.Enums;

namespace Jassi.Repositories
{
    public interface IMessageRepository
    {
        public Task<DbResult> CheckAndAddMessage(Message_AddRequest messageRequest);
    }

}
