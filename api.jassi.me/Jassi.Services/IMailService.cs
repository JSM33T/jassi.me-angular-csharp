using Jassi.Entities.Shared;

namespace Jassi.Services
{
    public interface IMailService
    {
        Task SendEmailAsync(EmailMessage emailMessage);
    }
}
