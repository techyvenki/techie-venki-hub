module Jekyll
    class PrevNextGenerator < Generator
      safe true
      priority :lowest
  
      def generate(site)
        site.collections.each do |_, collection|
          # Skip if not a collection we want to process
          next unless collection.label =~ /system_design|computing_models|cloud_services|cloud_native|data_ai/
          
          # Sort pages by nav_order
          sorted_docs = collection.docs.sort_by { |doc| doc.data['nav_order'] || Float::INFINITY }
          
          sorted_docs.each_with_index do |doc, index|
            # Set previous page
            if index > 0
              doc.data['prev_page'] = sorted_docs[index - 1].url
              doc.data['prev_page_title'] = sorted_docs[index - 1].data['title']
            end
            
            # Set next page
            if index < sorted_docs.length - 1
              doc.data['next_page'] = sorted_docs[index + 1].url
              doc.data['next_page_title'] = sorted_docs[index + 1].data['title']
            end
          end
        end
      end
    end
  end