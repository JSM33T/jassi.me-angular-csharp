using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Jassi.Services
{
    public interface INotificationService
    {
        Task SendNotificationAsync(string message);
    }
}
