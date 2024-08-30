﻿using Jassi.Entities.Dedicated;
using Jassi.Entities.DTO;
using Jassi.Entities.Shared;

namespace Jassi.Repositories
{
    public interface IBlogRepository
    {
        public Task<PaginatedResult<Blog_GetBlogs>> GetPaginatedBlogsAsync(Blog_GetRequest request);
        public Task<List<BlogCategory>> GetCategories();
        public Task<Blog> GetBlogDetailsBySlug(string Slug);
        public Task<IEnumerable<BlogAuthor>> GetBlogAuthorsByBlogId(int BlogId);
    }
}
