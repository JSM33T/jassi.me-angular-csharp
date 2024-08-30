using Jassi.Entities.DTO;
using Jassi.Entities.Enums;

namespace Jassi.Repositories
{
    public interface IUserRepository
    {
        public Task<User_ClaimsResponse> UserLogin(User_LoginRequest request);
        public Task<(DbResult, User_ClaimsResponse)> UserSignup(User_SignupRequest request);
    }
}
